import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')  # 网址输入必须带协议 http https

time.sleep(5)

driver.quit()
