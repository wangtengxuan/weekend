#测试框架是干嘛的
#最主要的用途是组织和执行测试用例
#导入unitest框架
import unittest
#java中的类和文件名的关系，public的类名和文件名一样
#python中的可以一样。但是推荐：文件名首字母小写，类名首字母大写，剩下一样
#2.集成unitest中的父类
#python中的继承直接用小括号
#TestCase是测试用例的意思，我们就在UnitestDemo中编写测试用例
class UnitestDemo(unittest.TestCase):
    #重写父类中的方法
    #def是方法的关键字
    #setUp是创建的意思
    #类似于手动测试中的预制条件
    def setUp(self):
        print("这个方法将会在测试用例执行前执行")
    def tearDown(self):
        print("这个方法将会在测试用例方法之后执行")
    #编写测试用例的方法
    #只有以test的开头命名的方法才是测试用例的方法
    #测试用例方法可以直接被运行
    #普通方法不能直接运行，只有被调用才能执行
    def test_login(self):
        print("登录的测试用例")
        self.zhuce()
    def zhuce(self):
        print("注册的测试用例")
    def test_search(self):
        print("搜索测试用例")
#如果你直接执行这个文件，那么就会执行下面的语句
#否则你执行其他文件时，import下面的代码就不会执行
if __name__ == '__main__':
    #执行当前文件中所有的unitest的测试用例
    #unittest.main()
    UnitestDemo.zhuce()
