import time
from selenium import webdriver

# 创建driver对象
driver = webdriver.Chrome()
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
# 打开指定URL
driver.get(url)

# 通过css选择器的方式定位元素
input01 = driver.find_element_by_css_selector('#userA')
input01.send_keys("zhangsan")
time.sleep(3)
# 关闭浏览器
driver.quit()
