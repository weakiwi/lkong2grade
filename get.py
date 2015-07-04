#coding=utf-8

import urllib2
import urllib
from bs4 import BeautifulSoup

url='http://www.yousuu.com/book/1'
response=urllib2.urlopen(url)
soup=BeautifulSoup(response.read())
tag=soup.find("div","col-sm-7")
tag=tag.get_text("|")
f=open("test.txt","a")
f.write(tag.encode('utf-8'))
f.close()
fp=open('test.txt','w')
lines=open('test.txt').readlines()
for s in lines:
    fp.write(s.replace('|','\r'))
fp.close()