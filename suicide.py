# -*- coding:UTF-8 -*-
import requests,sys, time
from bs4 import BeautifulSoup


class downloader(object):
	"""docstring for downloader"""
	def __init__(self,url,size):
		self.url = url
		self.size = size
		self.cookie = {"Cookie": '_T_WM=cdae6207b0c0f7a262e9935642bfe20c; MLOGIN=1; SCF=AjfLJHx6uqOp8rfLVuir1rPr12woa9vPR_ABR-ulMgEVVGhxTtLhtirXdof8rp6E9VItbyKewsyj3MAFbc3TUIQ.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhHY1fLcF0G0RFGfyD1-P6s5JpX5KzhUgL.Fo-ESKBRe0.7Son2dJLoI7ybMrLydrB7e7tt; M_WEIBOCN_PARAMS=lfid%3D102803_ctg1_8999_-_ctg1_8999_home%26luicode%3D20000174; SUB=_2A25xDsUhDeRhGeNM7lYZ8yfMzTSIHXVS8OtprDV6PUJbkdBeLW_2kW1NThsXGFGJBbxIkRqpjT4zwoATGdlHaHTF; SUHB=0Elqd7oR38Zzbj; SSOLoginState=1544205681'}
		self.target = 'http://www.biqukan.com/1_1094'
		self.names = []         #存放章节名
		self.urls = []			#存放章节链接
		self.nums = 0           #章节数

	def get_urls(self):
		for i in range(self.size):
			self.urls.append(self.url + str(i))
	def get_download_url(self):
		req=requests.get(url=self.target)
		html=req.text
		bf=BeautifulSoup(html)
		tests=bf.find_all('div', class_ = 'listmain')
		a_bf=BeautifulSoup(str(tests[0]))
		a=a_bf.find_all('a')
		self.nums = len(a[15:]) #剔除不必要的章节，并统计章节数
		for each in a[15:]:
		    self.names.append(each.string)
		    self.urls.append(self.server + each.get('href'))
	def get_contents(self, target):
		# print(target)
		req=requests.get(url=target)
		html=req.text
		bf=BeautifulSoup(html)
		texts=bf.find_all('div', class_ = 'showtxt')
		texts=texts[0].text.replace('\xa0'*8,'\n\n')
		return texts
	def get_comments(self):
		# print(target)
		for i in range(self.size):
			req=requests.get(url=self.urls[i],cookies = self.cookie)
			html=req.text
			bf=BeautifulSoup(html)
			texts=bf.find_all('div', class_ = 'c')
			# texts=texts[0].text
			for x in texts:
				cid = x.get('id')
				
				if cid != None and len(str(cid))>5:
					print (cid,type(cid))
					content = BeautifulSoup(str(x))
					print (content.find_all('span', class_ = 'ctt')[0].text)
			# print (texts)
			# break
			time.sleep(0.1)
		return texts

	def writer(self, name, path, text):
		write_flag = True
		with open(path, 'a', encoding='utf-8') as f:
			f.write(name + '\n')
			f.writelines(text)
			f.write('\n\n')
		


if __name__ == '__main__':
	dl=downloader(url = 'https://weibo.cn/comment/H66fjqVKi?uid=1537790411&rl=0&page=',
				size = 1000)
	dl.get_urls()
	print(dl.urls)
	dl.get_comments()
	# for i in range(5):
	# 	dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
	# 	sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
	# 	sys.stdout.flush()
	# print('《一年永恒》下载完成')

