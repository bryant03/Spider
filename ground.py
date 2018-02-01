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
        self.Plinks = []
        self.links = []
        for i in range(1,2):
            self.Plinks.append(self.url + str(i) + ".html")
    def get_links(self):
        for i in range(len(self.Plinks)):
            print (i,self.Plinks[i])
            req = requests.get(url=self.Plinks[i])
            html = req.text
            bf = BeautifulSoup(html,"html.parser")
            texts = bf.find_all('div', class_ = 'land-square-item')
            # print(type(texts))
            # print (texts[0])
            a_bf = BeautifulSoup(str(texts),"html.parser")
            a= a_bf.find_all('a')
            # print (type(a),len(a))
            for i in range (len(a)):
                if(i%2 == 1):
                    self.links.append(a[i].get('href'))
        print (self.links,len(self.links))
        self.downloadDetails(self.links[0])

    def downloadDetails(self,url):
        d = dict()
        req = requests.get(url=url)
        html = req.text
        bf1 = BeautifulSoup(html,"html.parser")
        text1 = bf1.find_all('div', class_ = 'bpic-max')
        print (text1)
        bf2 = BeautifulSoup(str(text1),"html.parser")
        text2 = bf2.find_all('li')
        print (type(bf2))
        for i in range (len(text2)):
            bf3 = BeautifulSoup(str(text2[i]),"html.parser")
            text3 = bf3.find_all('img')        
            print(text3[0].get('data-original'))


        text_title = bf1.find_all('div', class_ = 'landD-supply-pshow-tit')
        bf_title =  BeautifulSoup(str(text_title),"html.parser")
        text_title = bf_title.find_all('h1')
        print (text_title[0].text.replace('<h1>',"").replace('</h1>',""))

        result_groundPrice = bf1.find_all('p', class_ = 'font-18 text-warning padding-l-0')
        print (result_groundPrice)
        # print (text_title[0].text.replace('<h1>',"").replace('</h1>',""))
               

        

if __name__ == '__main__':
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    print (type(data[0]))
    a = dict()
    a['1'] = 'sasd'
    print(a)
    a = download()
    a.generateIds()
    a.get_links()
