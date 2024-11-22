import requests

# url ="https://www.baidu.com"
#
# proxies = {
#     "http" : "http://61.160.202.88:80",
#     'http': "http://42.63.65.89:80"
# }
#
# response = requests.get(url,proxies = proxies)
# print(response.request.headers)


# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}
# ip = "127.0.0.1"
# port = 8080
# proxies = {
#     "http": "http://%s:%d" % (ip, port),
#     "https": "http://%s:%d" % (ip, port)
#
# }

proxies = {
    "http" : "http://61.160.202.88:80",
    'http': "http://42.63.65.89:80"
}

url = "http://httpbin.org/ip"
response = requests.get(url, headers=headers, proxies = proxies)
print(response.json())
