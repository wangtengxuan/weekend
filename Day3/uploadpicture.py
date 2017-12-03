#1.登录，2.商品管理 3.添加商品，4
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/p[4]/input").click()
driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
#有种特殊的网页，比如左边或者上边有一个导航条，这时候就要注意了
#属于嵌套页面，其中’商品管理‘和’添加商品‘属于页面根节点的网页
#商品名称属于frame框架里的子网页
#之前使用过窗口切换，但是是用于不同网页之间的切换
#现在也需要切换网页
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("小米")
driver.find_element_by_id("1").click()
driver.find_element_by_css_selector('[id="2"]').click()
driver.find_element_by_id("6").click()


#双击是特殊的元素操作，所有的特殊操作被封装到Actionchains这个类中
#列表结束必须要用perform方法结尾
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
#driver.find_element_by_css_selector("#jiafen").click()
#driver.find_element_by_css_selector('[value="1"]').click()
driver.find_element_by_link_text("商品图册").click()
#有些页面控件是javascript的页面加载之后生成的，
#implicitily——wait是用来判断整个网页是否加载完毕
#有时页面加载完，但是javascript的控件还没有创建好，所以需要time.sleep（）提高程序的稳定性
time.sleep(2)
#driver.find_element_by_css_selector("#filePicker label").click()
#因为真正负责上传文件的页面元素是<input type="file"...
#所以我们可以直接操作这个控件
#这个控件可以直接输入图片的路径
driver.find_element_by_name("file").send_keys("D:/oup.png")
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
#alert这个控件不是直接弹出来的，需要时间等待
time.sleep(3)
driver.switch_to.alert.accept()
driver.find_element_by_class_name("button_search").click()

#页面太长，点击不了下面button,操作滚动条
#range（10）表示0到9，默认从0开始，到长度-1结束，一共10个数字
ac=ActionChains(driver)
for ittt in range(10):
    ac.send_keys(Keys.ARROW_DOWN)
ac.perform()
#javascript像素定位
driver.execute_script("window.scrollTo(200,100)")