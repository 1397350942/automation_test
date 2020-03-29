import unittest


def add(a, b):
    return a + b


# 继承unittest.TestCase类
class TestCase01(unittest.TestCase):
    # 在每条用例执行前执行
    def setUp(self) -> None:
        print("setUp")

    # 在每条用例执行后执行
    def tearDown(self) -> None:
        print("tearDown")

    # 方法名必须以test开头
    def testcase_01(self) -> None:
        print("testcase_01")
        print("1+1=", add(1, 1))
        # self.assertEqual(2, add(1, 2))

    def testcase_02(self) -> None:
        print("testcase_02")
        print("2+2=", add(2, 2))

    #
    def testcase_03(self) -> None:
        print("testcase_03")
        print("3+3=", add(3, 3))


class TestCase02(unittest.TestCase):
    # 方法名必须以test开头
    def testcase_01(self) -> None:
        print("TestCase02_testcase_01")

    def testcase_02(self) -> None:
        print("TestCase02_testcase_02")

    def testcase_03(self) -> None:
        print("TestCase03_testcse_03")


if __name__ == '__main__':
    unittest.main()
