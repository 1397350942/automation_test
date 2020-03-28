import time
from selenium import webdriver

# 创建driver对象
driver = webdriver.Chrome()
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
# 打开指定URL
driver.get(url)


input04 = driver.find_elements_by_tag_name("input")[3]
input04.send_keys("wengwenyu888@aliyun.com")
time.sleep(1)

time.sleep(3)
# 关闭浏览器
driver.quit()
