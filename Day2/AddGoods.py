#1.登录，2.商品管理 3.添加商品，4
from selenium import webdriver
from selenium.webdriver import ActionChains

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
driver.find_element_by_css_selector('[value="1"]').click()
