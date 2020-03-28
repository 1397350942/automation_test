import time
from selenium import webdriver

# 创建driver对象
driver = webdriver.Chrome()

time.sleep(1)

url = r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html"
# 打开指定的url
driver.get(url)
time.sleep(2)

# print("size:", driver.find_element_by_id("AAA").size)
# print("text:", driver.find_element_by_id("AAA").text)
# print("属性值:", driver.find_element_by_id("AAA").get_property("href"))
# print("当前页面title:", driver.title)
# print("当前url:",driver.current_url)

print("span标签是否可见:", driver.find_element_by_tag_name("span").is_displayed())
print("标签是否可用:", driver.find_element_by_id("cancelA").is_enabled())
time.sleep(2)
driver.quit()
