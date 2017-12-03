import unittest
#1.导入ddt代码库
import ddt
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Day4.readCsv2 import read

#2.装饰这个类
@ddt.ddt
class MemberManage(unittest.TestCase):
#3.调用之前写好read方法，获取配置文件中的数据
    member_info=read("member_info.csv")
    #global driver
    #在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前只执行一次")
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("测试登录")
        driver=self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password")\
        .send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()
    #python中的*号，表示把集合中的所有元素拆开，一个一个写
    #list=["小明","小红"]
    #*list="小明","小红"
    #把
    #假如一个方法需要接收两个参数，那么肯定不能传一个listjinq
    #但是如果list中正好也是两个元素，这时在列表前面加一个*
    #
    #@add.data()测试数据来源于read（）方法
    #把数据中的每一行传入方法，在方法中增加参数
    @ddt.data(*member_info)
    def test_b_add_member(self,row):
        #每组测试数据就算一组测试用例，每条测试用例应该是独立的，不能因为上一条测试用例失败，导致下一组数据不能正常被执行，所以不能用for循环
       #应该用ddt装饰器取装饰这个类，达到每条测试用例独立执行的目的
        #ddt是数据驱动测试  data driver test
        print("添加会员")

    #4.注释掉for循环，改变代码的缩进，是方法中的代码比方法中的声明缩进4个空格，快捷键：shift+空格
       # for row in read("member_info.csv"):
            #print("添加会员%s"%row)
       # time.sleep(3)
        driver = self.driver
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        #如果frame没有name属性时，我们可以通过其他方式定位iframe标签，把定位好的页面元素传
        # 给driver.switch_to.frame(iframe_html)方法也可以实现切换
        iframe_css="#mainFrame"
        iframe_html=driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector('[value="{0}"]'.format(row[2])).click()
        driver.find_element_by_name("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        #之前的代码是能够自动运行，但是还不能自动判断程序运行的是否正确
        #我们自动化代码，不能找人总是看着运行
        #actual实际结果，执行测试用例后，页面上实际显示的结果
        actual=driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        #expected期望结果，来自于手动测试用例，或者是需求文档，配置文件
        expected=row[0]
        #断言类似于if....else...,是用来做判断的
        # if(actual==expected):
        #     print("测试通过")
        # else:
        #     print("测试失败")
        #断言叫assert,断言是框架提供的，要想调用断言，那么必须加上self.，因为测试用例类继承了框架中的Testcase类，也继承了这个类中断言
        #断言有几个特点：
        #1.和if..else相比断言比较简洁
        #2.断言关注错误的测试用例
        #3.只有断言出错的时候，才会打印信息，正确时没有任何信息
        #断言报错时，后面的代码将不会继续执行，前面的步骤失败，后面的步骤就不需要继续尝试了，浪费性能
        #
        self.assertEqual(actual,expected)
    #切换到父框架
        #driver.switch_to.parent_frame()
   #切换到网页的默认内容（根节点）
        driver.switch_to.default_content()

if __name__ == '__main__':
    unittest.main()