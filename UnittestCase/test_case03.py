# coding = utf-8
import requests
import unittest
url = "http://www.imooc.com"
data = {
    "username": "zhangsan",
    "password": "123456"
}


class TestCase03(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case结束执行")

    @classmethod
    def setUpClass(cls):
        print("case类开始执行")

    @classmethod
    def tearDownClass(cls):
        print("case类执行结束")

    def test_07(self):
        print("执行case07")
        flag = "qwertyuiop"
        s = "asd"
        self.assertIn(s, flag, msg="不包含")
        pass

    def test_01(self):
        # res = requests.get(url=url, params=data).json()
        data1 = {
            "user": "123456"
        }
        self.assertDictEqual(data1, data, msg="这两个字典不相等")
        print("case01")

    def test_02(self):
        data1 = {
            "user": "123456"
        }
        data2 = {
            "user": "123456"
        }
        self.assertDictEqual(data1, data2)
        print("case02")

    def test_03(self):
        flag = True
        self.assertFalse(flag)
        print("case03")

    def test_04(self):
        flag = True
        self.assertTrue(flag)
        print("case04")

    def test_05(self):
        flag = "123"
        flag1 = "321"
        self.assertEqual(flag, flag1)
        print("case05")

    def test_06(self):
        flag = "qwertyuiop"
        s = "asd"
        self.assertIn(s, flag, msg="不包含")


if __name__ == "__main__":
    pass
