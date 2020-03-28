import time
from selenium import webdriver

driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')  # 网址输入必须带协议 http https
driver.get(r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html")
time.sleep(3)

driver.quit()
