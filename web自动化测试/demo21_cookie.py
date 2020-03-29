import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https:www.baidu.com")
time.sleep(1)

print(driver.get_cookies())
driver.add_cookie({"name": "BDUSS",
                   "value": "UFxOGdsfjhGb3JtcmJNaWVMeUFUS1lqSDBXd3U4alZEeTBWRWVvTTByNmpsYWRlRVFBQUFBJCQAAAAAAAAAAAEAAADrOiUzutqwtdbQ0bDV0tDSuKMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKMIgF6jCIBeM"})
driver.refresh()  # 刷新
time.sleep(3)
driver.quit()
