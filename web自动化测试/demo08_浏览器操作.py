import time
from selenium import webdriver

# 创建driver对象
driver = webdriver.Chrome()
# 浏览器窗口最大化
driver.maximize_window()
time.sleep(1)

url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
# 打开指定的url
driver.get(url)
time.sleep(1)

# # 设置浏览器大小(单位像素px)
# driver.set_window_size(800, 600)
# time.sleep(1)
# # 设置浏览器位置(单位像素px,以屏幕左上角为起点)
# driver.set_window_position(500, 300)
# a = driver.find_element_by_id("AAA")
# a.click()
# time.sleep(1)
#
# # 回退
# driver.back()
# time.sleep(1)
#
# # 刷新
# driver.refresh()
# time.sleep(1)
#
# # 前进
# driver.forward()

a1 = driver.find_element_by_id('fwA')
a1.click()

time.sleep(3)
driver.close()  # 关闭当前浏览器
time.sleep(2)
# 关闭整个浏览器
driver.quit()
