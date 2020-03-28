import time
# 导包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 创建driver对象
driver = webdriver.Chrome()
action = ActionChains(driver)

url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
driver.get(url)
time.sleep(1)

userA = driver.find_element_by_id("userA")
userA.send_keys("admin")
# 右击
action.context_click(userA).perform()
time.sleep(1)
# 双击
action.double_click(userA).perform()

time.sleep(2)
driver.quit()
