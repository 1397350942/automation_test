import requests

# 给接口地址定义一个变量
url = "http://apis.juhe.cn/simpleWeather/query"
params = {
    "city": "北京",
    "key": "e1b3b19b2ddc9aeec3247f07f3020689"
}
# 发送请求
result = requests.get(url=url, params=params)
print(result.status_code)

# 获取json数据
print(result.json())
result_json = result.json()
print(result_json.get("reason"))
print(result_json.get("result"))
print(result_json.get("error_code"))
