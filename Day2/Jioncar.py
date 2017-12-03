import time
from  selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
#driver=webdriver.Ie()
driver.get("http://localhost/")
#impliocitly含蓄，委婉
driver.implicitly_wait(30)
driver.maximize_window()
#点击登录按钮之前，要从javascript中删除target属性
#javascript定位方式比selenium麻烦
#如何用selenium的定位方式来替换jav的定位方式
#用arguments关键字，把元素定位作为一个参数，替换到javascript语句中
login_link=driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("wangtengxuan")
driver.find_element_by_id("password").send_keys("123456")
#submit（）用与提交表单，from是html中的一个元素
#from表单的任何子孙节点都可以通过submit（）方法提交表单
driver.find_element_by_id("password").submit()
#等待
#time.sleep(5)
#隐式等待，会自动判断网页是否加载完毕，当加载完毕立刻开始执行后续的操作
#我们需要设置最大时间，不能让程序无线等待，一般这个时间是30秒
#隐式等待，一经设置，对后面的所有语句都有效果，所以在创建浏览器时设置一次就ok了(在顶部)
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#iphoneImg=driver.find_element_by_css_selector("body > div.w1170.catalogue > div > div.catalogue-pro > div > a")
#body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a
#body > body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img
#img是标签名，>标签前面是父节点，后面是子节点
#如果想在css中写class属性，那么签名需要加上小数点
#：nth-child(2),表示当前节点在家中排老2，父亲的第二个儿子
#为什么我们要把css selector中的内容改的越短越好
#涉及到越多的节点，那么代码的健壮性和可维护性就越差
#因为开发一旦修改页面时，修改了这些节点，那么元素就会定位失败
iphoneImg=driver.find_element_by_css_selector("div.shop_01-imgbox > a")
driver.execute_script("arguments[0].removeAttribute('target')",iphoneImg)
iphoneImg.click()
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("惠谷")
driver.find_element_by_name("address[mobile]").send_keys("13800000000")
driver.find_element_by_id("add-new-area-select").click()
#driver.find_element_by_xpath('//*[@id="add-new-area-select"]')
#css定位
# driver.find_element_by_id("add-new-area-select").find_element_by_css_selector('[value="620000"]').click()
# driver.find_element_by_css_selector('[value="620100"]').click()
# driver.find_element_by_css_selector('[value="620104"]').click()
#方法二：
#下拉框是一种比较特殊的元素，selenium专门为下拉框提供了一种定位方式
#需要把这个元素从webelement类型转换成Select类型
#Select是selenium专门为我们创建的一个类
shen=driver.find_element_by_id("add-new-area-select")
Select(shen).select_by_value("620000")
shen.click()
#定位到第二个下拉框
city=driver.find_elements_by_tag_name("select")[1]
Select(city).select_by_index(1)
city.click()
qu=driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_visible_text("西固区")
qu.click()
driver.find_element_by_name("address[address]").send_keys("东京花园")
tijiao=driver.find_element_by_class_name("add-new-name-span-3").send_keys("1008611")
driver.find_element_by_class_name("aui_state_highlight").submit()