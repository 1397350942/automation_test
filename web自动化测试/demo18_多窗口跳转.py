import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
driver.get(url)
time.sleep(1)

# 获取当前窗口句柄
print("当前页:",driver.current_window_handle)
# 获取全部窗口句柄
print("所有:",driver.window_handles)

driver.find_element_by_id("fwA").click()
print("关闭原页面前:",driver.window_handles)
time.sleep(1)

# 跳转到新的窗口
# driver.switch_to.window(driver.window_handles[1])
print(driver.current_window_handle)
driver.find_element_by_id('kw').send_keys("python")

driver.close()
print("关闭原页面后:",driver.window_handles)
time.sleep(3)
driver.quit()
