import requests
from bs4 import BeautifulSoup


url = "https://weixin.sogou.com/weixin?_sug_type_=1&type=2&query=python"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}

response = requests.get(url,headers = headers).text
soup = BeautifulSoup(response,"lxml")
# 方法一
# ui_tag = soup.select(".news-list")
# h3_list = ui_tag[0].select("h3")
# for h3 in h3_list:
#     print(h3.select("a")[0].get_text(),h3.select("a")[0].get("href"))

h3_list = soup.find_all("h3") # 找到全部的h3
for h3 in h3_list:
    print(h3.select("a")[0].get_text(),h3.select("a")[0].get("href"))