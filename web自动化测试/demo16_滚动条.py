import time
# 导包
from selenium import webdriver

# 创建driver
driver = webdriver.Chrome()
driver.set_window_size(500, 600)
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"

driver.get(url)
time.sleep(1)

# 向下滚动1000单位
script = "window.scrollTo(0,1000)"
driver.execute_script(script)
time.sleep(2)

# 向右滚动1000单位
script = "window.scrollTo(1000,1000)"
driver.execute_script(script)

time.sleep(2)
driver.quit()
