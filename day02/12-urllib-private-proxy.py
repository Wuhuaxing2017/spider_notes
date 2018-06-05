import urllib
from urllib import request

# 私密代理格式username:password@server
username = os.environ.get('name')
pw = os.environ.get('password')
proxy
# proxies = {'http':'455098435:lbrv3bgb@47.92.75.71:187'}

proxyHandler = urllib.request.ProxyHandler(proxies = proxies)
opener = urllib.request.build_opener(proxyHandler)
