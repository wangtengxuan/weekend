import  unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Day5.myTestCase import MyTestCase
from Day6.data_base.connectD import connDB


class ZhuCeTest(MyTestCase):
    def test_zhu_ce(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element_by_name("username").send_keys("圣诞节")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("userpassword2").send_keys("123456")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("13800000001")\
        .send_keys(Keys.TAB).send_keys("123654@qq.com").send_keys(Keys.ENTER).perform()
        #检查数据库中新增的记录用户名和我们输入的用户名是否一致
        expected="圣诞节"
        actual=connDB()[1]
        self.assertEqual(expected,actual)
        print(connDB()[1])

