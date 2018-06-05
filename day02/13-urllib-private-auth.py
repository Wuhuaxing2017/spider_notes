import urllib
from urllib import request
import os

uri = os.environ.get('proxyServer')
user = os.environ.get('proxyuser')
pw = os.environ.get('password')

# 私密代理设置，Realm远程服务器域信息
# 密码管理器
pw_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

pw_mgr.add_password(None,uri='test',user='test',passwd='test')
handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(handler)

# 第一种，使用opener方式
response = opener.open(fullurl='http//www.baidu.com/')
print(response.read().decode('utf-8'))