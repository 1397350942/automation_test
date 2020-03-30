import requests
import unittest
from demo08_read_excel import Read_Ex


class WeatherTest(unittest.TestCase):
    def setUp(self) -> None:
        print("开始")

    def tearDown(self) -> None:
        print("结束")

    def test01(self):
        res1 = Read_Ex()
        data = res1.read_excel()
        for i in data:
            # 接口地址
            url = "http://apis.juhe.cn/simpleWeather/query"
            # 构造数据
            para = {"city": i.get("city"), "key": i.get("key")}
            res = requests.get(url=url, params=para)
            r = res.json()
            self.assertEqual(r["error_code"], int(i['exp']))


if __name__ == '__main__':
    unittest.main()
