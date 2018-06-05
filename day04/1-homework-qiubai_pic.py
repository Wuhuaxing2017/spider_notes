import requests
import re
import time
import urllib
import urllib.request

url_first = 'https://www.qiushibaike.com/pic/'
url = 'https://www.qiushibaike.com/pic/page/%d/'

data = '''
'<div class="thumb">

<a href="/article/120491686" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12049/120491686/medium/app120491686.jpg" alt="你是不是太激动了">
</a>

</div>
'''

def parseHtml(html):
	# re.S的作用忽略换行，将所有的数据作为整体进行匹配
	pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?</div>',re.S)
	img = pattern.findall(html)

	
	# 下载图片
	downloadImage(img)

def downImage(imgs):
	for img_url in imgs:
		filename = img_url.resplit(sep='/',maxsplit=1)[-1]
		urllib.request.urlretrieve('http:'+img_url,'./download/%s'%(filename))

		print('图片%s下载成功！'%(filename))

def loadhtml(page):
	if page == 1:
		url_html = url_first
		response = requests.get(url_html)
		response.encoding = 'utf-8'
		html = response.text

		# 使用正则解析HTML页面的url
		parseHtml(html)
	else:
		for i in range(1,page+1):
			if i == 1:
				url_html = url_first
			else:
				url_html = url%(i)
			response = requests.get(url_html)
			response.encoding = 'utf-8'
			html = response.text

			# 使用正则解析HTML页面的url
			parseHtml(html)
			time.sleep(60)

if __name__ == '__main__':
	page = int(input('请输入爬取图片的页数：'))
	loadhtml(page)
