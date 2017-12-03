import time

from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://localhost/")
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element_by_link_text("登录").click()
cwh=driver.current_window_handle
hwc=driver.window_handles
for item in hwc:
    if item==cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_id("username").send_keys("wangtengxuan")
#Chains链表和数组不同，数组有固定长度，链表必须有明确的结束语
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
#driver.find_element_by_css_selector("body  form > ul > li:nth-child(5) > input").click()
#点击账号设置
driver.find_element_by_link_text("账号设置").click()
driver.find_element_by_partial_link_text("个人资料").click()
#clear清空的意思，用来清空元素中文本的内容
#好的编程习惯，每次执行sendkeys之前，都进行一边clear操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("陈果汉")
#css可以用多个属性组合定期一个元素
#一个元素的多个属性之前不能有空格
driver.find_element_by_css_selector('#xb[value="1"]').click()
#方法一
#javascript是单独的语言，和python的语法不一样，不能直接在pycharm中执行
# js='document.getElementById("date").removeAttribute("readonly")'
# driver.execute_script(js)
# driver.find_element_by_id("date").clear()
# driver.find_element_by_id("date").send_keys("2017-1-1")
#方法二“
#用seleinum的定位方式 ，定位元素之后，对元素执行javascript脚本，删除readonly属性
data=driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',data)
data.clear()
data.send_keys("2007-7-7")
#方法三
#用seleinum调用javascript一共两个关键字
#1.arguments[0] :表示用python语言代替一部分javas
#好处是，有时，seleinum定位比较容易
#2.return把javas的执行结果返回给python语言
#好处，有时seleinum定位不到的元素，我们可以用javascript定位到
# date=driver.execute_script("return document.getElementById('date')")
# #data这句话==data=driver.find_element_by_id("date")
# date.click()
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("123456789")
driver.find_element_by_class_name("btn4").click()
#右键检查不了html代码弹出框，叫做alert，有单独方法处理
time.sleep(3)
#alert空间不是html代码生成的，所以implicitly——wait这个控件不管用
#所以就算上面写了智能等待，这个time.sleep()方法不能生效
#切换到alert方法，和切换窗的方法类似
#alert弹出框，accept 接受， 同意 确定 dismiss 拒绝， 取消
driver.switch_to.alert.accept()