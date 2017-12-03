#有了mytestcase以后，在写测试用例，就不需要重新写setUP和teraDown方法了
import os

from selenium import webdriver

from Day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    #三个双引号，表示文档字符串，也属于一种注释，和普通的区别，这种注释会显示在文档中
    """注册模块测试用例"""
    #因为myTestCaes已经实现了setup金额tearDowm方法，我们以后在学测试用例就不需要重新实现setup和teardown方法了
    def test_zhe_ce(self):
        """打开注册页面的测试用例"""
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        #用来获取当前浏览器的网址
       # driver.current_url
        #用来获取当前浏览器中的标签页的title
        actual=driver.title
        expected="用户注册 - 道e坊商城 - Powered by Haidao"
        #截取整个浏览器的图片
        base_path=os.path.dirname(__file__)
        #把day5替换成图片保存路径
        path=base_path.replace('Day5','report/image/')
        driver.get_screenshot_as_file(path+"zhuce.png")
        self.assertEqual(actual,expected)