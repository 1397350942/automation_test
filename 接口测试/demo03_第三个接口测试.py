import requests

# 定义接口地址 天气预报 天气种类
url = "http://apis.juhe.cn/simpleWeather/wids"
params = {
    "key": "e1b3b19b2ddc9aeec3247f07f3020689"  # 正确的key
}
result = requests.get(url=url, params=params).json()

print(result)
print(result.get("result"))
print(result.get("error_code"))
