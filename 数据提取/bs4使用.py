from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">xixixi</p>
"""

# 创建Soup对象
soup = BeautifulSoup(html, 'lxml')
# 查找所有的a标签
print(soup.find_all('a'))
# 查找第一个a标签
print(soup.find("a"))
# 根据正则表达式查找
print(soup.find_all(re.compile("^c")))
# 传入列表查找任一元素
print(soup.find_all(["a", "b"]))

# attrs参数
# 传入字典，{"属性名":"属性值"}，根据标签属性搜索对应的值 参数attrs
print(soup.find_all(attrs = {"class" : "title"}))
print(soup.find_all(class_ = "title"))
print(soup.find_all(id = "link1"))

#  string参数,通过string参数搜索文档中的字符串内容
print(soup.find_all(string="Elsie"))
print(soup.find_all(string= ["Tillie","Elsie","Lacie"]))
print(soup.find_all(re.compile("^Dormouse")))

# css选择器
print(soup.select("b"))# 搜索标签直接写
print(soup.select(".title")) # 类标签用.
print(soup.select("#link3"))# id标签加
print(soup.select("body p a "))# 层级选择器，可以用空格也可以用>
print(soup.select("body>p>a "))# 层级选择器，可以用空格也可以用>
print(soup.select("[class = 'title']"))  # 属性选择器
print(soup.select(".title")[0].get_text())  # 获取文本
print(soup.select("a")[0].get('href')) # 获取属性的值
print(soup.select("p")[0].get('name')) # 获取属性的值