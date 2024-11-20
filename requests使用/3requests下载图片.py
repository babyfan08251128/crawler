import requests

# 获取百度logo图片
url = 'https://www.baidu.com/img/bd_logo1.png'

response = requests.get(url).content

with open('baidu.png',"wb") as f:
    f.write(response)