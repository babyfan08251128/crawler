import requests
url = "https://www.baidu.com"

response = requests.get(url)
print(response)
print(response.status_code)
print(response.content)
print(response.text)
print(response.content.decode('utf-8'))
print("-" * 100)
# 打印请求头
print(response.request.headers)
print(response.headers)
print("-" * 100)
# print(response.request.cookies)
# 打印set-cookies
print(response.cookies)
# 打印URl
print(response.url)

