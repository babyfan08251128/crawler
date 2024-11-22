import jsonpath
info = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
            {"category": "fiction",
             "author": "Herman Melville",
             "title": "Moby Dick",
             "isbn": "0-553-21311-3",
             "price": 8.99
             },
            {"category": "fiction",
             "author": "J. R. R. Tolkien",
             "title": "The Lord of the Rings",
             "isbn": "0-395-19395-8",
             "price": 22.99
             }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}

# 1. 提取第1本书的title
book1_title = jsonpath.jsonpath(info,"$..book[0].title")[0]
print(book1_title)
# 2. 提取2、3、4本书的标题
book2_title = jsonpath.jsonpath(info,"$..book[1:4].title")
print(book2_title)
# 3. 提取1、3本书的标题
book3_title = jsonpath.jsonpath(info,"$..book[0,2].title")
print(book3_title)
# 4. 提取最后一本书的标题
book4_title = jsonpath.jsonpath(info,"$..book[-1:].title")
print(book4_title)
book4_title_1 = jsonpath.jsonpath(info,"$..book[(@.length-1)].title")
print(book4_title_1)
# 5. 提取价格小于10的书的标题
book5_title = jsonpath.jsonpath(info,"$.store.book[?(@.price < 10)].title")
print(book5_title)
# 6. 提取价格小于或者等于20的所有商品的价格
book6_title = jsonpath.jsonpath(info,"$.store.book[?(@.price <= 20)].title")
print(book6_title)
# 7. 获取所有书的作者
bok7 = jsonpath.jsonpath(info,"$..book[::].author")
book7_1 = jsonpath.jsonpath(info,"$.store.book[*].author")
print(bok7)
# 8. 获取所有作者
book8 = jsonpath.jsonpath(info,"$..author")
print(book8)
# 9. 获取在store中的所有商品(包括书、自行车)
book9 = jsonpath.jsonpath(info,"$.store")
print(book9)
# 10. 获取所有商品（包括书、自行车）的价格
book10 = jsonpath.jsonpath(info,"$..price")
print(book10)
# 11. 获取带有isbn的书
book11 = jsonpath.jsonpath(info,"$..book[?(@.isbn)].title")
print(book11)
# 12. 获取不带有isbn的书
book12 = jsonpath.jsonpath(info,"$..book[?(!@.isbn)].title")
print(book12)
# 13. 获取价格在5~10之间的书
book13 = jsonpath.jsonpath(info,"$..book[?(@.price > 5 and @.price < 10)].title")
print(book13)
# 14. 获取价格不在5~10之间的书
book14 = jsonpath.jsonpath(info,"$..book[?(@.price < 5 or  @.price > 10)].title]")
print(book14)
# 15. 获取所有的元素
book15 = jsonpath.jsonpath(info,"$.*")
print(book15)