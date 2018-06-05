import urllib
from urllib import request

url = ''

# 使用Charles抓包获取ajax真实的url，请求这类数据和之前网络请求是一样的
def loadmovie(start,limit,page):
	for p in range(page):
		url_movie = url%(start,limit)
		request = urllib.request.Request(url=)


if __name__ == '__main':
	start = int(input('请输入起始查询索引：'))
	end = ''