#!/usr/bin/env python
# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import urllib.error
import pymysql
def xiazai_mzitu(url):
    html = urllib.request.urlopen(url)
    title = BeautifulSoup(html.read(),'lxml').find("h2",{"class":"main-title"}).get_text()
    title = title.replace(':','')
    html = urllib.request.urlopen(url)
    page = BeautifulSoup(html.read(),'lxml').find("div",{"class":"pagenavi"}).findAll("span")[-2].get_text()
    try:
        os.makedirs("D:\\temp\\pic\\mzitu\\"+title)
    except:
        return 
    after = int(page)+1
    for i in range(1,after):
        try:
            url1 = url + '/' + str(i)
            html = urllib.request.urlopen(urllib.request.Request(url1))
            picurl = BeautifulSoup(html.read(),'lxml').find("div",{"class":"main-image"}).find("img")["src"]
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
            f = open("D:\\temp\\pic\\mzitu\\"+title+"\\"+str(i)+".jpg","wb")
            f.write(img)                 
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()                                                                             
                sql = ("insert into url(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()      
                cur.close()        
                conn.close() 
                print('未下载网址已存入数据库')
                continue
            if hasattr(e,"reason"):
                print(e.reason)
                conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()                                                                             
                sql = ("insert into url(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()      
                cur.close()        
                conn.close()
                print('未下载网址已存入数据库')
                continue
def xiazai_mzitu_sql(url):
    html = urllib.request.urlopen(url)
    title = BeautifulSoup(html,'lxml').find("h2",{"class":"main-title"}).get_text()
    title = title.replace(':', '.')
    html = urllib.request.urlopen(url)
    page = BeautifulSoup(html,'lxml').find("div",{"class":"pagenavi"}).findAll("span")[-2].get_text()
    try:
        os.makedirs("D:\\temp\\pic\\mzitu\\"+title)
    except:         
        shutil.rmtree("D:\\temp\\pic\\mzitu\\"+title)
        os.makedirs("D:\\temp\\pic\\mzitu\\"+title)
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
            f = open("D:\\temp\\pic\\mzitu\\"+title+"\\"+str(i)+".jpg","wb")
            f.write(img)                 
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
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
                conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()
                sql = ("insert into urll(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()
                cur.close()
                conn.close()
                print('未下载网址已存入数据库')
                continue
if __name__ == '__main__':
    for i in range(1,162):
        print("第"+str(i)+"页")
        allurl = 'http://www.mzitu.com/page/'+str(i)+'/'
        allhtml = urllib.request.urlopen(allurl).read()
        alltitles = BeautifulSoup(allhtml,'lxml').findAll('ul')[-1].findAll("a")
        title = []
        for alltitle in alltitles:
            title.append(alltitle['href'])
        alltitle = list(set(title))
        for eachtitle in alltitle:
            url = eachtitle+'/'
            print(url)
            xiazai_mzitu(url)
    urls = []
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
    cur = conn.cursor()
    cur.execute("select url from url")
    results = cur.fetchall()
    cur.close()
    conn.close()
    result = list(results)
    for r in result:
        urls.append("%s"%r)
    urls = list(set(urls))
    while urls:
        url = urls.pop()
        print("重新下载:%s"%url)
        xiazai_mzitu_sql(url)
        try:
            conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
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

