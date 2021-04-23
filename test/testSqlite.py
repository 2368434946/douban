#-*- codeing = utf-8 -*-
#@Time : 2021/3/30 13:22
#@Author : 刘也
#@File : testSqlite.PY
#@Software : PyCharm


import sqlite3
#打开或创建数据库文件
conn = sqlite3.connect("test.db")
print("成功打开数据库")
#获取游标
c = conn.cursor()

# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
#
#
#
# '''

# sql = '''
#    insert into company(id,name,age,address,salary)
#    values(1,'张三',32,"成都",8000)
# '''


sql = '''
   select id,name,address,salary from company
'''

#执行sql语句
cursor = c.execute(sql)
for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary =",row[3],"\n")


#提交数据库操作
conn.commit()
#关闭数据库连接
conn.close()
# print("成功建表")