import time
from selenium import webdriver

# 创建driver对象
driver = webdriver.Chrome()
url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
# 打开指定URL
driver.get(url)

# link1 = driver.find_element_by_link_text("AA 百度 网站") #必须写完整的文本内容
# link1.click()
link2 = driver.find_element_by_partial_link_text("AA")# 可以写部分内容
link2.click()

time.sleep(3)
# 关闭浏览器
driver.quit()
