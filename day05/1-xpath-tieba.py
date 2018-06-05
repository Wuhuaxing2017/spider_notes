import requests
from lxml import etree

url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%s'
url_base = 'http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%d'
url_lz = 'http://tieba.baidu.com/p/%d'


def loadtieba(key,page_start,page_end):
	headers = {'User-Agent':'asds;fasdf'}
	for i in range(page_start,page_end+1):
		url = url_base%(key,(i-1)*50)
		response = requests.get(url=url,headers=headers)
		print(response.encoding)

		html = response.text
		# 解析HTML数据
		xpathParse(html)

def xpathParse(html):
	html_tree = etree.HTML(html)

	lzs = html.xpath('//div[@class="t_con cleafix"]')	






if __name__ == '__main__':
	key = input('输入关键字：')
	page_start = input(input('起始页：'))
	page_end = input(input('终止页：'))

	# 该方法加载贴吧数据，
	loadtieba(key,page_start,page_end)