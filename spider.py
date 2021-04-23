# -*- codeing = utf-8 -*-
# @Time : 2021/3/20 9:03
# @Author : 刘也
# @File : spider.PY
# @Software : PyCharm


from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    # savepath = "豆瓣电影Top250.xls"
    dbpath = "movie.db"
    # 保存数据
    # saveData(datalist, savepath)
    saveData2DB(datalist,dbpath)

    # askURL("https://movie.douban.com/top250")


# 创建正则表达式对象，表示规则（字符串的模式）
# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片的链接  re.S 让换行符包含在字符中
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    # 调用获取页面信息的函数，10次
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        # 保存获取到的网页源码
        html = askURL(url)
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        # 查找符合要求的字符串，形成列表
        for item in soup.find_all('div', class_="item"):
            # 保存一部电影的所有信息
            data = []
            item = str(item)
            # re库用来通过正则表达式查找指定的字符串
            # 影片详情的链接
            link = re.findall(findLink, item)[0]
            # 添加链接
            data.append(link)
            # 添加图片
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            # 添加片名，片名可能只有一个中文名，没有外国名
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
            # 添加中文名
                ctitle = titles[0]
                data.append(ctitle)
            # 添加外国名并去掉无关的符号
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
            # 外文名留空
                data.append(' ')
            # 添加评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            # 添加评价人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            # 添加概述
            inq = re.findall(findInq, item)
            if len(inq) != 0:
            # 去掉句号
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
            # 留空
                data.append(" ")
            # 添加影片的相关内容
            bd = re.findall(findBd, item)[0]
            # 去掉<br/>
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            # 替换 /
            bd = re.sub('/', " ", bd)
            # 去掉前后的空格
            data.append(bd.strip())

            # 把处理好的一部电影信息放入datalist
            datalist.append(data)


    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {
        "User-Agent": "Mozilla / 5.0(iPhone;CPU iPhoneOS 13_2_3 like Mac OS  X) AppleWebKit / 605.1.15(KHTML, likeGecko) Version / 13.0.3Mobile / 15E148Safari / 604.1"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 3.保存数据
def saveData(datalist, savepath):
    print("save....")

    # 创建workbook对象
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    # 创建工作表
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    # 写入数据 第一个参数：行 第二个参数：列 第三个参数：内容
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" %(i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    # 保存数据表
    book.save(savepath)










#保存数据

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' +data[index]+'"'

        sql = '''
                insert into movie250 (info_link, pic_link, cname, ename, score, rated, instroduction, info) 
                values(%s)'''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close
    conn.close()
def init_db(dbpath):
    #创建数据表
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        
        )
    
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':  # 当程序执行时

    # 调用函数
    # init_db("movietest.db")
    main()

    print("爬取完毕")