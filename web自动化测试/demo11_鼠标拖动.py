import time
# 导包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 创建driver对象
driver = webdriver.Chrome()
# 创建action对象
action = ActionChains(driver)
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\drag.html"
driver.get(url)
time.sleep(1)

source = driver.find_element_by_id("div1")
target = driver.find_element_by_id("div2")
time.sleep(1)
action.drag_and_drop(source, target).perform()

time.sleep(2)
driver.quit()
