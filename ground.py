# -*- coding:UTF-8 -*-
import requests,json,time,sys, os
from contextlib import closing
from bs4 import BeautifulSoup
class download(object):
    """docstring for get_photos"""
    def __init__(self):
        self.url = "http://www.tuliu.com/gongying/nongcun/list-pg"

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
        # self.downloadDetails(self.links[0])

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
        d ['img'] = []
        for i in range (len(text2)):
            bf3 = BeautifulSoup(str(text2[i]),"html.parser")
            text3 = bf3.find_all('img')        
            print(text3[0].get('data-original'))
            d['img'].append(text3[0].get('data-original'))


        text_title = bf1.find_all('div', class_ = 'landD-supply-pshow-tit')
        bf_title =  BeautifulSoup(str(text_title),"html.parser")
        text_title = bf_title.find_all('h1')
        print (text_title[0].text.replace('<h1>',"").replace('</h1>',""))
        d['title'] = text_title[0].text.replace('<h1>',"").replace('</h1>',"")

        result_landPrice = bf1.find_all('p', class_ = 'font-18 text-warning padding-l-0')
        price = ""
        if len(result_landPrice) != 0:
            print (result_landPrice)
            price = result_landPrice[0].text
        elif len(bf1.find_all('div', class_ = 'col-sm-9 font-18 text-warning padding-l-0')) != 0:
            print (bf1.find_all('div', class_ = 'col-sm-9 font-18 text-warning padding-l-0'))
            price = bf1.find_all('div', class_ = 'col-sm-9 font-18 text-warning padding-l-0')[0].text
        else :
            pass
            
        d['landPrice']= price
        

        result_landPromise = bf1.find_all('div', id = 'take_look_fee_1')
        if len(result_landPromise) != 0:
            d["landPromise"] = result_landPromise[0].text

        result_landTakeLook = bf1.find_all('div', id = 'take_look_fee_0')
        if len(result_landTakeLook) != 0:
            d["landTakeLook"] = result_landTakeLook[0].text

        result_landPosition = bf1.find_all('div', class_ = 'col-sm-9 text-gray-4')
        # print (result_landPosition)
        # print (result_landPosition[0].text)

        d['landPosition'] = result_landPosition[0].text


    
        result_landType = bf1.find_all('div', class_ = 'col-sm-2 text-gray-4')
        # print (result_landType)
        # print (result_landType[0].text)
        d['landType'] = result_landType[0].text
        # print (result_landType[1].text)
        d['landArea'] = result_landType[1].text


        result_landUse = bf1.find_all('div', class_ = 'col-sm-4 text-gray-4')
        # print (result_landUse)
        # print (result_landUse[0].text)
        d['landUse'] = result_landUse[0].text
        # print (result_landUse[1].text)
        d['landYearLimitation'] = result_landUse[1].text

        


        result_landDescription = bf1.find_all('div', class_ = 'landD-intr-txt')
        # print (result_landDescription)
        # print (result_landDescription[0].text)
        d['result_landDescription'] = result_landDescription[0].text

        result_landPeople = bf1.find_all('p', class_ = 'text-gray-2 padding-b-15 font-18')
        d['landPeople'] = result_landPeople[0].text
        
        result_landPhone = bf1.find_all('p', id = 'land_display_phone')
        print (result_landPhone)
        print (d)
        # with open(file, 'a+') as f:
        # f.write(mobile+'\n')   #加\n换行显示



        

if __name__ == '__main__':
    # path= os.path.abspath('.')
    # path =path + os.sep+'img'
    # isExists=os.path.exists(path)
    # print (isExists)
    # if not isExists:
    #     os.makedirs(path) 
    
    
    # a = download()
    # a.generateIds()
    # a.get_links()
    # a.downloadDetails("http://taicang.tuliu.com/s-view-58614.html")

    s =  "http://huangzhou.tuliu.com/landext/view/30706/1"
    req = requests.get(url=s)
    print (req.text)

    s2 = "http://mengla.tuliu.com/landext/view/504936/2"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                'Referer' : 'http://mengla.tuliu.com/view-504936.html',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Accept': 'application/json, text/javascript, */*; q=0.01'}
    req = requests.get(url=s2,headers=headers)
    print (req.text)
    # /landext/view/58671/1


    s3 = "http://arongqi.tuliu.com/landext/view/58627/1"
    req = requests.get(url=s3)
    print (req.text)