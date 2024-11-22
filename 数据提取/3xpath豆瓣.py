import requests
from lxml import etree
url = "https://movie.douban.com/subject/1292052/comments?status=P"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
}

response= requests.get(url,headers = headers).content.decode('utf-8')
html = etree.HTML(response)
xpath_comment = "//*[@class = 'mod-bd']/div/div[2]/p/span/text()"
comment_list = html.xpath(xpath_comment)
print(comment_list)
print(f"共获取到{len(comment_list)}个评论")
for item in comment_list:
    print(item + "\n")