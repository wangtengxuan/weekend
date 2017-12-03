#javascript 是一门独立的语言
#学seleinum,三件事：
# 1元素地位：id--name---class
#link_text必须是链接，必须是<a>标签，必须是文本
# 2.元素的操作：鼠标左键单机click，发送键盘上的按键 send_keys
# 3.学好javascript
#javascript和python是两种不同的语言
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/")
js="document.getElementsByClassName('site-nav-right fr')[0].childNodes[1].removeAttribute('target')"
driver.execute_script(js)
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("wangtengxuan")
driver.find_element_by_id("password").send_keys("123456")