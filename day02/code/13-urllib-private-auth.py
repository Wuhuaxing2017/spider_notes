import urllib
import urllib.request
import os

uri = os.environ.get('proxyServer')
user = os.environ.get('proxyuser')
pw = os.environ.get('password')

# 另一种方式，进行私密代理设置

# Realm 远程服务器域信息
# 密码管理器
pw_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 向密码管理器中添加密码，proxyserver
# 参数一远程服务器域信息，一般None
pw_mgr.add_password(None,uri='slfjsfjlsa',user = 'slfjslfjlsa',passwd='123456')


handler = urllib.request.ProxyBasicAuthHandler()


opener = urllib.request.build_opener(handler)

# 第一种使用opener方式
response = opener.open(fullurl='http://www.baidu.com/')

print(response.read().decode('utf-8'))


# 第二种使用opener方式
# 全局的设置，opener对象参数，设置给urllib.request
# urllib.request.install_opener(opener)
#
# response = urllib.request.urlopen(url = 'http://www.baidu.com/')
#
# print(response.read().decode('utf-8'))