from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("登录").click()
dangqian=driver.current_window_handle
print("dangqian:%s"%dangqian)
suoyou=driver.window_handles
print("suoyou:%s"%suoyou)
for item in suoyou:
    if item==dangqian:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_id("username").send_keys("yuanliang")
driver.find_element_by_id("password").send_keys("654321")