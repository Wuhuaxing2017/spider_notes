import urllib
import urllib.request

# proxy 代理，使用代理，完成网络请求
# ProxyHandler 和 HttpHandler用法完全一样

# 代理，多个
proxies = {
           # 'socks':'110.73.33.207:6673',
           'http':'61.135.217.7:80'}

proxyHandler = urllib.request.ProxyHandler()

# 创建Opener
opener = urllib.request.build_opener(proxyHandler)


# 使用opener进行网络请求
url = 'http://www.baidu.com/'

request = urllib.request.Request(url=url)

response = opener.open(request)
print(response.read().decode('utf-8'))
