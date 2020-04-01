from selenium import webdriver
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# driver = webdriver.Edge()
url = "http://www.5itest.cn/register?goto=http%3A//www.5itest.cn/"
driver.get(url)
time.sleep(3)
driver.quit()
