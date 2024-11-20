import requests

session =requests.Session()

# 2. 创建一个headers
headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

# 使用session发送请求对象，会给第二次的请求自动添加服务器返回的cookie
response = session.get("https://www.baidu.com/")
# 打印请求头
print(response.request.headers)
# 打印响应头
print(response.headers)
# 打印服务器返回的cookies
print(requests.utils.dict_from_cookiejar(response.cookies))

# 再次请求
response = session.get("https://www.baidu.com/")
# 再次打印响应头
print(response.request.headers)

