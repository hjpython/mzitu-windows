#!/usr/bin/env python
# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import urllib.error
import pymysql
def rename_mzitu(url):
    html = urllib.request.urlopen(url)
    title = BeautifulSoup(html.read(),'lxml').find("h2",{"class":"main-title"}).get_text()
    title = title.replace(':','.')
    html = urllib.request.urlopen(url)
    page = BeautifulSoup(html.read(),'lxml').find("div",{"class":"pagenavi"}).findAll("span")[-2].get_text()
    try:
        os.makedirs("D:\\temp\\pic\\mzitu\\"+title)
    except:
        os.rename("D:\\temp\\pic\\mzitu\\"+title,"D:\\temp\\pic\\mzitu\\"+title+page)
        return
if __name__ == '__main__':
    for i in range(3,4):
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
            rename_mzitu(url)
