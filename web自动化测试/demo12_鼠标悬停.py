import time
# 导包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 创建driver对象
driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(30)
# 窗口最大化
driver.maximize_window()

action = ActionChains(driver)
url = r'https://www.baidu.com'
driver.get(url)
more = driver.find_element_by_name('tj_briicon')
print(more)
# 鼠标悬停
action.move_to_element(more).perform()

time.sleep(2)
driver.quit()
