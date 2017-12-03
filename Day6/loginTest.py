import time
from selenium import webdriver


from Day5.myTestCase import MyTestCase
from selenium.webdriver.common.by import By

from Day6.page_object.Loginpage import LoginPage
from Day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
#1.打开网页
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp=LoginPage(self.driver)  #实例化一个登录页面
        lp.open()

#输入用户名

        #driver.find_element(By.ID,"username").send_keys("wangtengxuan")
        lp.input_username("wangtengxuan")
#输入密码
        #driver.find_element(By.ID,"password").send_keys("123456")
        lp.input_password("123456")
#点击登录按钮
        lp.denglu()
        #driver.find_element(By.CLASS_NAME,"login_btn").click()
        time.sleep(5)
#验证是否跳转到管理中心页面
        #expected="我的会员中心 - 道e坊商城 - Powered by Haidao"
        pc=PersonalCenterPage(self.driver)

#找到包含内容
        self.assertIn(pc.title,self.driver.title)