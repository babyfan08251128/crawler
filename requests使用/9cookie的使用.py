import requests

url = 'https://www.baidu.com'

response = requests.get(url)
# 获取到响应头中的cookie,是一个对象
print(response.cookies)
cookie = response.cookies
print(dict(cookie))
print(requests.utils.dict_from_cookiejar(response.cookies))
