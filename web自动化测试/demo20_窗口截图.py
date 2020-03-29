import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get(r"C:\Users\wengw\Documents\automation_test\web自动化测试\素材\注册A.html")
time.sleep(1)

driver.find_element_by_id("userA").send_keys("zhangsan")
# 给图片命名
# img_name = time.strftime("%Y%m%d_%H%M%S")
img_name = str(time.time()).replace(".", "_")
# 截图并生成图片
driver.get_screenshot_as_file("./images/%s.png" % img_name)

time.sleep(3)
driver.quit()
