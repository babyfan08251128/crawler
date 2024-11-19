import requests

url = 'https://www.360buy.com/'
headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

# response = requests.get(url, headers=headers, allow_redirects=False)
# print(response.request.url)  # https://www.360buy.com/
#
# response = requests.get(url, headers=headers, )
# print(response.request.url)  # https://www.jd.com/

# 获取历史请求信息
response = requests.get(url, headers=headers)
for info in response.history:
    print(info.status_code, info.url, info.headers)
