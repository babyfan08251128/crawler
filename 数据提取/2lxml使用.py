from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''


def test_etree():
    # 利用etree.HTML方法将文本转换为Element对象，Element对象具有XPath方法
    html = etree.HTML(text)
    print(type(html))

    handled_html = etree.tostring(html).decode("utf-8")
    print(handled_html)
    print(type(handled_html))


def test_get_href_txt():
    html = etree.HTML(text)
    title_list = html.xpath("//div/ul/li/a/text()")
    href_list = html.xpath("//div/ul/li/a/@href")
    for title, href in zip(title_list, href_list):
        item = dict()
        item[title] = href
        print(item)


if __name__ == '__main__':
    test_get_href_txt()
