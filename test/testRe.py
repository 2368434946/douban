#-*- codeing = utf-8 -*-
#@Time : 2021/3/29 21:36
#@Author : 刘也
#@File : testRe.PY
#@Software : PyCharm


#正则表达式;字符串模式（判断字符串是否符合一定的标准）
import re
#创建模式对象
#此处的AA，是正则表达式，用来去验证其他的字符串
pat = re.compile("AA")
#search字符串被校验的内容
# m =pat.search("CBA")

# m =pat.search("ABCAA")
# m =pat.search("AABCAA")

#没有模式对象
#前面的字符串是规则（模板），后面的字符串是被校验的对象
# m = re.search("asd","Aasd")
# print(m)

#前面的字符串是规则（正则表达式），后面的字符串是被校验的字符串

# print(re.findall("[A-Z]","ASDaDFGAa"))
# print(re.findall("[A-Z]+","ASDaDFGAa"))

#在第三个字符串中找到a用A替换
# print(re.sub("a","A","abcdcasd"))

#在正则表达式中，建议被比较的字符串前面加上r,不用担心转义字符的问题
a = r"\aabd-\'"
print(a)