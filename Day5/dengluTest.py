import unittest
from selenium import webdriver


class DengluTest(unittest.TestCase):
    """登录模块测试用例"""
    def setUp(self):
        #打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_denglu(self):
        """登录测试正常情况测试用例"""
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("wangtengxuan")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_class_name("login_btn").click()
        nihao=driver.find_element_by_link_text("您好 wangtengxuan").text
        self.assertEqual(nihao,"您好 wangtengxuan")
        print("当前用户名：陈果汉")