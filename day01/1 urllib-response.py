import urllib
from urllib import request, response
url = 'http://www.baidu.com/'

# 返回响应
response = urllib.request.urlopen(url=url)

content = response.read().decode('utf-8')
print(content)
