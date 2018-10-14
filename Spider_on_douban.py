from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os

class Moviepicture():

	def __init__(self):
		self.init_url = "https://movie.douban.com/top250"+"?start=225&filter="
		self.folder_path = "~/Desktop/Moviepicture"

	def  save_img(self,url,file_name):
		print('开始请求图片地址，过程会有点长。。。')
		img = requests.get(url)
		print('开始保存图片')
		f = open(file_name,'ab')
		f.write(img.content)
		print(file_name,'图片保存成功')
		f.close()

	def  request(self,url):
		r = request.get(url)
		return r

	def mkdir(self,path):
		path = path.strip()
		isExists = os.path.exists(path)
		if not isExists:
			print('创建名叫做', path,'的文件夹')
			os.makedirs(path)
			print('创建成功!')
			return True
		else:
			print(path,'文件已经存在了,不在创建')
			return False

	def spider(self):
		print("start!")
		driver = webdriver.PhantomJS(executable_path='/Users/hosen/Documents/PhantomJS/bin/phantomjs')
		driver.get(self.init_url)
		html = driver.page_source

		self.mkdir(self.folder_path)
		print('开始切换文件夹')
		os.chdir(self.folder_path)

		print('开始获取所有divpic标签')
		all_divpic = BeautifulSoup(html,'lxml').find_all("div",
		"pic")

		for divpic in all_divpic:
			movie_picture_url = divpic.find('img')['src']
			movie_name = divpic.find('img')['alt']
			print(movie_picture_url,movie_name)

			self.save_img(movie_picture_url,movie_name)
	


movie_picture=Moviepicture()
movie_picture.spider()