from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost")
# 窗口切换：把selenium切换到新的窗口切换
driver.find_element_by_link_text("注册").click()
# 浏览器当前窗口的句柄（名字）
cwh = driver.current_window_handle
# selenium只提供selenium工作窗口的名字，并没有提供第二个窗口的名字，我们要自己求

# 获取浏览器中所有窗口句柄
whs = driver.window_handles
# for关键字， item=集合中的某个元素，in=关键字  whs=数组/集合
# 所以item表示whs中的一个元素，每次循环取一个值，循环结束
# whs中每个元素都会被遍历一次
for item in whs:
    if item == cwh:
        #关闭窗口
        driver.close()
    else:
        #切换到第二个没有关闭的窗口
        driver.switch_to.window(item)

driver.find_element_by_name("username").send_keys("yuanliang")
driver.find_element_by_name("password").send_keys("654321")
driver.find_element_by_name("userpassword2").send_keys("654321")
driver.find_element_by_name("mobile_phone").send_keys("13800000000")
driver.find_element_by_name("email").send_keys("123@qq.com")
driver.find_element_by_class_name("reg_btn").click()
