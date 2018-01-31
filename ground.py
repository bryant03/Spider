# -*- coding:UTF-8 -*-
import requests,json,time,sys
from contextlib import closing
from bs4 import BeautifulSoup
class download(object):
    """docstring for get_photos"""
    def __init__(self):
        self.url = "http://www.tuliu.com/gongying/nongcun/list-pg"
        self.download_server='https://unsplash.com/photos/xxx/download?force=trues'
        self.target='http://unsplash.com/napi/feeds/home'
        self.headers={'authorization':'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
    def generateIds(self):
        self.Pids = []
        self.ids = []
        for i in range(1,101):
            self.Pids.append(self.url + str(i) + ".html")
    def get_ids(self):
        print (self.Pids[0])
        req = requests.get(url=self.Pids[0])
        print (req.text)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'land-square-item')
        print(type(texts))

if __name__ == '__main__':
    a = download()
    a.generateIds()
    a.get_ids()