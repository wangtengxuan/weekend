# 1.打开了浏览器
# 2.打开登陆界面
# 3.输入用户名
# 4.输入密码
# 5,点击登陆按钮

# 从seleinum中到处网洛驱动，用来操作浏览器的
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
#访问网址
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#网页上所有可见的都属于element,比如link,按钮，下拉框。。。
#id查找，找到用户名输入框的id，并且向页面元素发送王腾萱的按键
driver.find_element_by_id("username").send_keys("wangtengxuan")
driver.find_element_by_id("password").send_keys("123456")

#如果使用一个方法，这个方法没有提示信息，那么这个方法肯定不存在
driver.find_element_by_class_name("login_btn").click()
