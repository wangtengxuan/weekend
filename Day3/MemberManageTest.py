import unittest

import time
from selenium import webdriver
class MembersManagesTest(unittest.TestCase):
    #变量前面加上self，表示这个变量是类的属性，可以被所有的方法访问
    def setUp(self):
        #driver声明在setUp方法之内，不能被其他方法访问
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def tearDown(self):
        #close是关闭一个浏览器的标签
        #quit是关闭浏览器
        #代码编写和调试的时候需要在quit（）方法前放一个时间等待，方便看清楚执行过程
        #正式运行的时候去掉时间等待，为了提高程序执行速度
        time.sleep(20)
        pass
        #self.driver.quit()
    def test_add_member(self):
        #self.driver.get("")
        driver=self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/p[4]/input").click()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("卢克")
        driver.find_element_by_name("mobile_phone").send_keys("13800000000")
        driver.find_element_by_name("birthday").send_keys("2017-1-1")
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/dl/dd/div/div/dl/form/dd/ul/li[5]/input").send_keys("123@qq.com")
        driver.find_element_by_css_selector("body   dd > div > div > dl > form > dd > ul > li:nth-child(6) > input").send_keys("123456789")
