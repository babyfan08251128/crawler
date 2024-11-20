import requests

url = 'http://www.baidu.com/'

response = requests.get(url,stream=True)# 已字节流的形式下载文件，

with open('1.html','wb') as f:
    for chunk in response.iter_content(chunk_size=100):
        if chunk:
            f.write(chunk)

