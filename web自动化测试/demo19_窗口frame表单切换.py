import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(30)
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册实例.html"
driver.get(url)
time.sleep(1)

# 跳转到指定frame表单
driver.switch_to.frame("myframe1")
driver.find_element_by_id("fwA").click()
print("打开新窗口以后:", driver.window_handles)
# 跳转到新窗口
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
# 跳转回老窗口
driver.switch_to.window(driver.window_handles[0])
# 回到老窗口后,焦点默认在主页面
driver.switch_to.frame("myframe1")  # 切换到 myframe1
driver.find_element_by_id('userA').send_keys("zhangsan")

time.sleep(3)
driver.quit()
