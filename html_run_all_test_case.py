import os
import smtplib
import unittest
#HTMLTestRunner是基于unittest框架的一个扩展，可以自己在
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
   f=open(path,"rb")
   mail_body=f.read()
   f.close()
   #想发邮件要把二进制的内容转成MIME格式
   #MIME multipurse多用途，Interent互联网，Mail邮件，Extension 扩展
   #这种格式是对邮件协议的扩展，使邮件不仅支持文本格式，还支持多种格式，比如：图片，音频，二进制文件
   msg=MIMEText(mail_body,'html','utf-8')
   #上面是邮件的正文，但是对于一个邮件来讲，除了正文，还需要主题，发件人，收件人
   #msg是字典的类型，类似于数组，区别是：1.字典是无序的
   #dict={}
   msg["Subject"]=Header("自动化测试报告","utf-8")
   #如果想用客户端软件或者自己写代码登录邮箱，很多类型的邮箱，需要单独设置一个客户端授权码
   #为了邮箱安全着想
   #因为都没有设置授权码
   msg['From']='bwftest126@126.com'
   msg['To']='13893103204@163.com'
   #邮件内容准备ok，开始发送邮件
   #发邮件的手动步骤
   #1.打开登录页面（连接邮箱服务器）
   #要想链接服务器，首先必须搞清楚网络传输协议：http，https，ftp，socket
   #邮件的协议，一般有三种，要先看邮箱支持那种协议：pop3，smtp，imap
   #我们要选一种传输协议，用来发邮件:smtp
   #首先导入smtplib的代码库
   smtp=smtplib.SMTP() #实例化一个SMTP类的对象
   smtp.connect("smtp.126.com")#链接126邮箱服务器的地址
   #2.登录邮箱
   smtp.login("bwftest126@126.com","abc123asd654")
   #3.发送邮件
   smtp.sendmail("bwftest126@126.com","13893103204@163.com", msg.as_string())
   #4.退出邮箱
   smtp.quit()
   print("邮件发送成功")

if __name__ == '__main__':
    #时间戳:str=String,f=format格式
    #strftime()通过这个方法定义时间的格式
    now=time.strftime("%Y-%m-%d_%H-%M-%S")
    suite=unittest.defaultTestLoader.discover("./Day5","*Test.py")
    #unittest.TextTestRunner文本测试用的运行器
    #现在用html的测试用例运行器最终会生成一个html格式的测试报告
    #我们至少要指定测试报告的路径
    base_case=os.path.dirname(__file__)
    path=base_case+"/report/report"+now+".html"
    file=open(path,'wb')
    HTMLTestRunner(stream=file,title="海盗商城测试报告",description="测试环境：window server 2008 + Chrome").run(suite)
    # 当测试用例执行完成，我们应该生成一封测试邮件
    #我们要把html报告作为正文发送邮件
    file.close()
    send_mail(path)
    #这时生成的测试报告，只显示类名方法名，只能传给专业人士看
    #我们应该相关的手动测试用例的标题加到我们的测试报告
    #我们自动化测试用例是从手工测试用例中挑出来的，手工测试用例怎么写，我们就怎么编写代码，所以我们代码里应该可以体现手工测试用例的标题
    #新的测试报告会覆盖原来的测试报告，如果想把所有的测试报告保存起来要如何去做呢？
    #加一个时间戳，按照当前时间计算一个数字，把数字作为文件名的一部分，就避免了文件名重复的的问题
    #当测试用例执行完成，我们应该生成一封测试邮件