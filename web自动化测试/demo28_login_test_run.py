import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from demo27_iwebshop_login_test import IwebshopLoginTest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(IwebshopLoginTest))
with open("./reports/iwebshop_login_test_report.html", "wb") as f:
    h = HTMLTestRunner(stream=f, title="iwebshop登录模块自动化报告", description="Windows10 Chrome")
    h.run(suite)
