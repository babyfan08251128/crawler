import requests

url = 'http://www.cninfo.com.cn/new/disclosure'

header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "cookie": "JSESSIONID=969F1DA34E367916DCC3A5097D2CB659; SF_cookie_4=27783614; insert_cookie=37836164; _sp_ses.2141=*; _sp_id.2141=ea2e7545-1d2f-4a62-808c-7ef4cadc5516.1731987944.1.1731987944.1731987944.ce2a5e31-c055-4132-9b7d-a2c24837cc23",
    "referer": "http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice"
}
data = {
    "column": 'szse_latest',
    "pageNum": '1',
    "pageSize": '30',
    "sortName": '',
    "sortType": '',
    "clusterFlag": 'true',
}

response = requests.post(url, headers=header, data=data)
print(response.json())
