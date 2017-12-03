from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_css_selector("body > div.w1170.catalogue > div > div.catalogue-pro > div > a > img").click()
cwh=driver.current_window_handle
hwc=driver.window_handles
for item in hwc:
    if item==cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_id("joinCarButton").click()
