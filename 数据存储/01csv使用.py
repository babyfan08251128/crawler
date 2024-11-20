import csv

with open("test.csv","r",newline='') as f:
    # 创建一个csv对象
    reader = csv.reader(f)
    for row in reader:
        print(row)


with open("test.csv", 'r') as csvfile:
    # 返回一个迭代器，以字典的格式放回，key为列名，value为对应的值
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# 写入数据

headers = ['班级', '姓名', '性别', '手机号', 'QQ']

rows = [
    ["18级Python", '小王', '男', '13146060xx1', '123456xx1'],
    ["18级Python", '小李', '男', '13146060xx2', '123456xx2'],
    ["19级Python", '小赵', '女', '13146060xx3', '123456xx3'],
    ["19级Python", '小红', '女', '13146060xx4', '123456xx4'],
]

with open("1.csv","w") as csvfile:
    wirter = csv.writer(csvfile)
    wirter.writerow(headers)
    for row in rows:
        wirter.writerow(row)

rows = [
    {
        "class_name": "18级Python",
        "name": '小王',
        "gender": '男',
        "phone": '13146060xx1',
        "qq": '123456xx1'
    },
    {
        "class_name": "18级Python",
        "name": '小李',
        "gender": '男',
        "phone": '13146060xx2',
        "qq": '123456xx2'
    },
    {
        "class_name": "19级Python",
        "name": '小赵',
        "gender": '女',
        "phone": '13146060xx3',
        "qq": '123456xx3'
    },
    {
        "class_name": "19级Python",
        "name": '小红',
        "gender": '女',
        "phone": '13146060xx4',
        "qq": '123456xx4'
    },
]
fieldnames = []
for key, value in rows[0].items():
    fieldnames.append(key)
with open("2.csv","w") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(rows)
