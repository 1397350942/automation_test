"""
1. 导入selenium包 --> from selenium import webdriver
2. 导入time包 --> from time import sleep
3. 实例化火狐浏览器 --> driver=webdriver.Firefox()
4. 打开注册A.html --> driver.get(url)
5. 调用id定位方法 --> driver.find_element_by_id("")
6. 使用send_keys()方法发送数据 --> .send_keys("admin")
7. 暂停3秒 --> sleep(3)
8. 关闭浏览器 --> quit()
"""
import time
from selenium import webdriver

# 创建driver对象
driver = webdriver.Chrome()
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
driver.get(url)

input01 = driver.find_element_by_id("userA")
input01.send_keys("zhangsan")
time.sleep(1)

input02 = driver.find_element_by_name("passwordA")
input02.send_keys("12345678")
time.sleep(1)

input03 = driver.find_element_by_class_name("telA")
input03.send_keys("13683080000")
time.sleep(1)

input04 = driver.find_elements_by_tag_name("input")[3]
input04.send_keys("wengwenyu888@aliyun.com")
time.sleep(1)

time.sleep(3)
driver.quit()
