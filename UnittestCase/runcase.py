from UnittestCase.test_case03 import TestCase03
from UnittestCase.test_case02 import TestCase02
from UnittestCase.test_case01 import TestCase01
import unittest
import sys
sys.path.append("C:\\Users\\wengw\\Documents\\automation_test")


case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
case_03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)


if __name__ == "__main__":
    suote = unittest.TestSuite([case_01, case_02, case_03])
    unittest.TextTestRunner(suote)
    pass
