#-*- codeing = utf-8 -*-
#@Time : 2021/3/29 23:43
#@Author : 刘也
#@File : testXlwt.PY
#@Software : PyCharm

import xlwt
# #创建workbook对象
# workbook = xlwt.Workbook(encoding="utf-8")
# #创建工作表
# worksheet = workbook.add_sheet('sheet1')
# #写入数据 第一个参数：行 第二个参数：列 第三个参数：内容
# worksheet.write(0,0,'hello')
# #保存数据表
# workbook.save('student.xls')


#创建workbook对象
workbook = xlwt.Workbook(encoding="utf-8")
#创建工作表
worksheet = workbook.add_sheet('sheet1')
#写入数据 第一个参数：行 第二个参数：列 第三个参数：内容
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d" %((i+1),(j+1),(i+1) * (j+1)))
#保存数据表
workbook.save('九九乘法表.xls')