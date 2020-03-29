import time
import unittest
from selenium import webdriver


class IwebshopLoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://192.168.32.128/index.php")
        time.sleep(1)

    def test_login(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_name("login_info").send_keys("test_user")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_class_name("submit_login").click()
        login_info = self.driver.find_element_by_class_name("loginfo").text
        try:
            self.assertIn("test_user", login_info)
        except AssertionError as e:
            print("错误信息:", e)
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace(".", "_"))
            raise

    def test_login_error(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_name("login_info").send_keys("test_user2")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_class_name("submit_login").click()
        login_info = self.driver.find_element_by_class_name("loginfo").text
        try:
            self.assertIn("test_user1", login_info)
        except AssertionError as e:
            print("错误信息:", e)
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace(".", "_"))
            raise

    def tearDown(self) -> None:
        pass
