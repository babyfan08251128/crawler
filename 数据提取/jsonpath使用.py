import jsonpath

info = {
    "error_code": 0,
    "stu_info": [
        {
            "id": 2059,
            "name": "小白",
            "sex": "男",
            "age": 28,
            "addr": "河南省济源市北海大道xx号",
            "grade": "天蝎座",
            "phone": "1837830xxxx",
            "gold": 10896,
            "info": {
                "card": 12345678,
                "bank_name": '中国银行'
            }
        },
        {
            "id": 2067,
            "name": "小黑",
            "sex": "男",
            "age": 28,
            "addr": "河南省济源市北海大道xx号",
            "grade": "天蝎座",
            "phone": "87654321",
            "gold": 100
        }
    ]
}
# # 取某个学生姓名的原始方法:
# 获取name，bank_name

# 常规提取方式
name1 = info["stu_info"][0]["name"]
print(name1)
name2 = info["stu_info"][1]["name"]
print(name2)
bank_name1 = info["stu_info"][0]["info"]["bank_name"]
print(bank_name1)

# 使用jsonpath提取
name1 = jsonpath.jsonpath(info,"$.stu_info[0].name")[0]
print(name1)
name2 = jsonpath.jsonpath(info,"$.stu_info[1].name")[0]
print(name2)
name_list = jsonpath.jsonpath(info,"$..name")
print(name_list)
bank_name1 = jsonpath.jsonpath(info,"$.stu_info[0].info.bank_name")[0]
print(bank_name1)
bank_name2 = jsonpath.jsonpath(info,"$..bank_name")[0]
print(bank_name2)

#  练习

