import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    '''
    登录模块测试用例
    '''
    def setUp(self):
        #打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()