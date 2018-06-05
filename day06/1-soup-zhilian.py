import requests
from bs4 import BeautifulSoup

url_base = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&p=%d'

if __name__ == '__main__':
	city = input('请输入查询城市：')
	job = input('请输入查询工作：')
	page = input(input('请输入查询页码数量：'))
	url = url_base%(city,job,page)

	zhilian = Zhilian(url_base,city,job,page)
	zhilian.start()

class Zhilian(object):

	def __init__(self,url_base,city,job,page)->None:
		super().__init__()
		self.url = url_base
		self.city= city
		self.job = job
		self.page = page
		self.headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
		self.items = []

	# 爬虫启动
	def start(self):
		for i in range(1,self.page+1):
			url = self.url%(self.city, self.job, i)
			
			html = self.handle_url(url)
			self.soup_parse(html)

	def handle_url(self.url):
		response  requests.get(url = url,headers = sel


			