import requests

# URL = 'http://www.baidu.com/s'
#
# kw = {"wd": "python"}
# response = requests.get(URL, params=kw)
# print(response.request.url)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

url = 'https://www.baidu.com/s?wd=1'
response = requests.get(url, headers=headers)
print(response.content.decode())
