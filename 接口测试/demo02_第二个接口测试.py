import requests

# 给接口地址定义一个变量
url = "http://apis.juhe.cn/simpleWeather/query"
params = {
    "city": "北京",
    "key": "e1b3b19b2ddc9aeec3247f07"  # 错误的key
}
# 发送请求
result = requests.get(url=url, params=params)
error_code = result.json().get("error_code")
print(error_code)
