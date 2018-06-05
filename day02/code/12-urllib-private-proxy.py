import urllib
import urllib.request
# 保护密码，个人信息
# 保存计算机的环境变量中
import os

username = os.environ.get('proxyuser')
pw = os.environ.get('password')
proxyServer = os.environ.get('proxyServer')

print(username,pw,proxyServer)

# 私密代理格式username：password@server
proxies = {'http':'%s:%s@%s'%(username,'123456',proxyServer)}

proxyHandler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(proxyHandler)

url = 'http://www.baidu.com/'

response = opener.open(url)

print(response.read().decode('utf-8'))