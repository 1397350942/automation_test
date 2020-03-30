"""
新闻头条 https://www.juhe.cn/docs/api/id/235
"""
import requests
import unittest


class NewsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://v.juhe.cn/toutiao/index"
        print("开始")

    def test01(self):
        params = {
            "type": "top",
            "key": "0e021b176aa8851ff0feaf3cbec6a34f"
        }
        result = requests.post(url=self.url, params=params).json()
        # print(result)
        self.assertEqual(result.get("error_code"), 0)


if __name__ == '__main__':
    unittest.main()
