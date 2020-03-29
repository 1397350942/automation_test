import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(30)
driver.get(r'C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册实例.html')
time.sleep(1)

# 跳转到指定frame表单
driver.switch_to.frame('myframe1')
driver.find_element_by_id("userA").send_keys('zhangsan')
time.sleep(2)

# 跳转回默认父级页面
driver.switch_to.default_content()
# driver.switch_to.parent_frame()

driver.switch_to.frame("myframe2")
driver.find_element_by_id("userB").send_keys("adminB")


time.sleep(3)
driver.quit()