import requests


url = "https://chinasoftinc.com/owa"
# verify: 忽略证书错误
response = requests.get(url,verify=True)
print(response)