"""
需求：
    1. 通过脚本执行输入 用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com;
    2. 间隔3秒后，修改电话号码为：18600000000
    3. 间隔3秒，点击注册用户A
    4. 间隔3秒，关闭浏览器
    5. 元素定位方法不限
"""
import time
from selenium import webdriver

# 创建driver对象
driver = webdriver.Chrome()
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
# 打开指定url
driver.get(url)

text_list = [
    "admin",
    "123456",
    "18611111111",
    "123@qq.com"
]
inputs = driver.find_elements_by_css_selector("p>input")
for i in range(4):
    inputs[i].send_keys(text_list[i])
    time.sleep(1)

inputs[3].clear()  # 清除
time.sleep(1)
baidu_a = driver.find_element_by_css_selector("#AAA")
baidu_a.click()  # 点击
time.sleep(3)
# 关闭浏览器
driver.quit()
