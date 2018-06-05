import urllib
from urllib  import request,parse

url = 'https://www.baidu.com/s?wd=%E9%9B%AA%E8%8E%B2'
print(urllib.parse.unquote('%E9%9B%AA%E8%8E%B2'))

key = input("请输入查询的关键字：")

# 使用百度进行检索
k = urllib.parse.quote(key)

print(k)

url = 'http://www.baidu.com/s?wd=%s'%(k)

response = urllib.request.urlopen(url=url)

print(response.read().decode('utf-8'))