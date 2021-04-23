#-*- codeing = utf-8 -*-
#@Time : 2021/3/29 17:50
#@Author : 刘也
#@File : testUrllib.py.PY
#@Software : PyCharm


import urllib.request
# #获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# #对获取到的网页源码进行utf-8解码
# print(response.read().decode('utf-8'))

#获取一个post请求

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data= data)
# print(response.read().decode("utf-8"))


#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)


# url = "http://httpbin.org/post"
# headers = {"User-Agent":" Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
#
# }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url = "https://www.douban.com"
headers = {"User-Agent":" Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"

}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))