import urllib
import urllib.request

user = 'Michael'
pw = '123456'

uri = 'http://10.11.58.219:80'

# HTTPBasicAuthHandler,密码管理器
pw_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

pw_mgr.add_password(None,uri=uri,user = user,passwd = pw)

web_auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr=pw_mgr)

# 使用handler创建opener
opener = urllib.request.build_opener(web_auth_handler)

# 将opener安装到全局，直接可以使用urllib.request.urlopen()
urllib.request.install_opener(opener)


response = urllib.request.urlopen(url= 'http://10.11.58.219:80')

print(response.read().decode('utf-8'))