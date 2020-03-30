import requests

url = "http://apis.juhe.cn/simpleWeather/cityList?key="
params = {
    'key': "e1b3b19b2ddc9aeec3247f07f3020689"
}
result = requests.post(url=url,params=params).json()
print(result.get("result"))