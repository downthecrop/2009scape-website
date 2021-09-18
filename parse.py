# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

from os import listdir
from os.path import isfile, join

mypath = "C:\\Users\\Anon\\Projects\\2009scape-website\\services\\m=news\\archives"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
 
url = 'http://localhost:8000/services/m=news/archives/2020-11-19.html'


for f in onlyfiles:
    url = "http://localhost:8000/services/m=news/archives/" + f
    print(url)
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    
    ## Jekyll
    tmp = open("test/"+f, "w")
    tmp.write('---\n')
    tmp.write('title: '+soup.title.string+'\n')
    tmp.write('tags: news'+'\n')
    tmp.write('layout: newspost'+'\n')
    tmp.write('collection: Game Updates'+'\n')
    tmp.write('date: '+f[:-5]+"00:00:00 +0000"+'\n')
    tmp.write('authors: '+soup.find("div", {"class": "msgcreator uname"}).text.strip())

    tmp.write('---\n')
    for hit in soup.findAll(attrs={'id' : 'content'}):
        tmp.write(unidecode(str(hit)))
    tmp.close()
    