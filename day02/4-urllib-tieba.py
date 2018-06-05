import urllib
import urllib.request

url = ''

key = input('请输入关键字：')
page_start = input('起始页：')
page_end = input('结束页：')

headers = {'User-Agent':''}

key = urllib.parse.quote(key)

page_start = int(page_start)
page_end = int(page_end)

for i in range(page_start,page_end+1):
	url_tieba = url%(kw,(i-1)*50)
	request = urllib.request.Request(url = url_tieba,headers = headers)
	response = urllib.request.urlopen(request)
	content = response.read().decode('utf-8')

	with open('./download/')