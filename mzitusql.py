#!/usr/bin/env python
# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import os
import urllib.error
import shutil
import pymysql
def xiazai_mzitu_sql(url):
    html = urllib.request.urlopen(url)
    title = BeautifulSoup(html,'lxml').find("h2",{"class":"main-title"}).get_text()
    html = urllib.request.urlopen(url)
    page = BeautifulSoup(html,'lxml').find("div",{"class":"pagenavi"}).findAll("span")[-2].get_text()
    try:
        os.makedirs(r"/home/hj/python/pic/mzitu/"+str(title))
    except:         
        shutil.rmtree(r"/home/hj/python/pic/mzitu/"+str(title))
        os.makedirs(r"/home/hj/python/pic/mzitu/"+str(title))
    after = int(page)+1
    for i in range(1,after):
        try:
            url1 = url + str(i)
            html = urllib.request.urlopen(urllib.request.Request(url1))
            picurl = BeautifulSoup(html,'lxml').find("div",{"class":"main-image"}).find("img")["src"]
            req = urllib.request.Request(picurl)
            req.add_header("Accept","image/webp,image/apng,image/*,*/*;q=0.8")
            req.add_header("Accept-Encoding","gzip,deflate")
            req.add_header("Accept-Language","zh-CN,zh;q=0.8")
            req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36")
            req.add_header("Cookie","Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1512579081,1512617737; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1512617750")
            req.add_header("Referer","http://www.mzitu.com/111061/13")
            req.add_header("Connection","keep-alive")
            req.add_header("Host","i.meizitu.net")
            img = urllib.request.urlopen(req).read()
            f = open("/home/hj/python/pic/mzitu/"+title+"/"+str(i)+".jpg","wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                conn = pymysql.connect(host='192.168.0.131',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()
                sql = ("insert into urll(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()
                cur.close()
                conn.close()
                print('未下载网址已存入数据库')
                continue
            if hasattr(e,"reason"):
                print(e.reason)
                conn = pymysql.connect(host='192.168.0.131',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()
                sql = ("insert into urll(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()
                cur.close()
                conn.close()
                print('未下载网址已存入数据库')
                continue
urls = []
conn = pymysql.connect(host='192.168.0.131',user='root',passwd='123456',db='mypydb',charset='utf8')
cur = conn.cursor()
cur.execute("select url from url")
results = cur.fetchall()
cur.close()
conn.close()
result = list(results)
for r in result:
    urls.append("%s"%r)
urls = list(set(urls))
print(len(urls))
urls.remove('http://www.mzitu.com/57773/')
print(len(urls))
while urls:
    url = urls.pop()
    print("重新下载:%s"%url)
    xiazai_mzitu_sql(url)
    try:
        conn = pymysql.connect(host='192.168.0.131',user='root',passwd='123456',db='mypydb',charset='utf8')
        cur = conn.cursor()
        cur.execute("select url from urll")
        results = cur.fetchall()
        cur.execute("truncate urll")
        cur.close()
        conn.close()
        result = list(results)
        for r in result:
            urls.append("%s"%r)
        urls = list(set(urls))
    except:
        pass

