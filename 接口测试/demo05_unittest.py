import requests
import unittest


class WeatherTest(unittest.TestCase):
    def setUp(self) -> None:
        self.url = "http://apis.juhe.cn/simpleWeather/query"
        self.params = {}
        print("开始")

    def tearDown(self) -> None:
        print("结束")

    def test01(self):
        self.params = {
            "city": "北京",
            "key": "e1b3b19b2ddc9aeec3247f07f3020689"  # 正确的key
        }
        result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(result.get("reason"), "查询成功!")

    def test02(self):
        self.params = {
            "city": "北京",
            "key": "e1b3b19b2ddc9aeec324"  # 错误的key
        }
        result = requests.get(url=self.url, params=self.params).json()
        self.assertEqual(result.get("reason"), "错误的请求KEY")


if __name__ == '__main__':
    unittest.main()
