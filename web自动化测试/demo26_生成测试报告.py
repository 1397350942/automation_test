import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from demo22_unittest_testcase import TestCase01

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestCase01))
with open("./reports/report01.html",'wb') as f:
    h = HTMLTestRunner(stream=f, title="测试报告", description="windows chrome")
    h.run(suite)
