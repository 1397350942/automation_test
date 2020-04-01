from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "http://www.baidu.com"
driver.get(url)
time.sleep(3)
driver.quit()
