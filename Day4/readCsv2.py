#1.之前的readcsv不能被其他测试用例调用，所以应该给这段代码封装到一个方法里
import csv
#2.每个测试用例的路径不同，所以path应该作为参数传入到这个方法中
#3.我们打开了一个文件，但是没有关闭，最终会造成内存泄露
import os


def read(filename):
    # 4.这个路径是一个绝对路径，我们工作，一个项目不止一个人编写代码
    # 我们没法统一要求大家都把项目代码放在一个路径下，因为有的人可能会放在其他盘
    # 这个文件因为在项目中，他的路径也会随着项目变化
    # 所以应该在代码中,通关当前当代码文件的两年，自动找到相对路径
    # path = r"C:\Users\51Testing\PycharmProjects\weekend\data\member_info.csv"
    # 所以首先要找到当前文件的路径
    # os是操作系统，path是路径，dir是目录，
    # __file__是paython内置的变量，指的是当前文件
    #所以重复的代码的出现，都是程序设计不合理
    #重复的代码应该封装到一个方法里
    current_file_path = os.path.dirname(__file__)
    print(current_file_path)
    # 我们正在想要的路径是csv文件的路径
    path = current_file_path.replace("Day4", "data/"+filename)
    print(path)
   # file=open(path,"r")
    #with语句是一个代码块，代码块的内容都要缩进4个空格
    #with代码块可以自动关闭with中声明的变量file
    #因为file文件一旦被关闭，里面的数据也随着消失
    #所以单独声明一个列表result，来保存里面的数据
    result=[]
    with open(path,'r')as file:
         data_table=csv.reader(file)
         for row in data_table:
            #print(row)
            result.append(row)
    return result
        #如果在打开和关闭程序的代码中间发生了异常，导致后面的代码不能正常运行
        #file.close()也不执行，这时文件任然不能关闭
        #file.close()
        #应该用with语句实现文件关闭
if __name__ == '__main__':
    #read("member_info.csv")
    me=read("member_info.csv")
    print(me)
#5.读出数据不是目的，目的是通过数据驱动测试，所以应该把数据作为方法的返回值方便进一步调用





