import urllib
import urllib.request

# 经过认证，https，没有数据
# http就可以获取数据
url = 'https://www.baidu.com/'

# https 添加header可以访问数据

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

# pycharm 万能键Alt + Enter
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))