import unittest


def add(a, b):
    return a + b


class TestCase01(unittest.TestCase):
    def testcase_01(self) -> None:
        print("testcase_01")
        print("1+1=", add(1, 1))
        self.assertEqual(2, add(1, 2))
        # try:
        #     self.assertEqual(2, add(1, 2))
        # except AssertionError as e:
        #     print("报错信息", e)
        #     raise

    # def testcase_02(self) -> None:
    #     print("testcase_02")
    #     print("2+2=", add(2, 2))
    #     try:
    #         self.assertIn("124", "123456")
    #     except AssertionError as e:
    #         print(e)
    #         raise
    #
    # def testcase_03(self) -> None:
    #     print("testcase_03")
    #     print("3+3=", add(3, 3))


if __name__ == '__main__':
    unittest.main()
