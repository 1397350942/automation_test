import time
# 导包
from selenium import webdriver
from selenium.webdriver.support.select import Select

# 创建driver对象
driver = webdriver.Chrome()
url = r'C:\Users\wengw\Documents\automation_test\web自动化测试\素材\css_example.html'
# 打开指定的url
driver.get(url)
time.sleep(1)

# 获取元素并点击
driver.find_element_by_xpath("/html/body/input[1]").click()
# 切换到alter弹框(或者说拿到弹窗对象)
alter = driver.switch_to.alert
time.sleep(1)
# 进行操作
alter.accept()
time.sleep(1)
# 获取元素并点击
driver.find_element_by_xpath("/html/body/input[2]").click()
# 切换到alter弹窗
alter = driver.switch_to.alert
time.sleep(1)
# 进行取消操作
print(alter.text)
alter.dismiss()
time.sleep(1)
# 获取元素并点击
driver.find_element_by_xpath("/html/body/input[3]").click()
# 切换到alter弹窗
alter = driver.switch_to.alert
time.sleep(1)
print(alter.text)
time.sleep(2)
# 进行操作
alter.dismiss()
time.sleep(3)
driver.quit()
