import urllib
import urllib.request

import http.cookiejar as cookiejar

import urllib.parse

# 创建cookiejar对象，保存访问网络的cookie
cookie = cookiejar.CookieJar()

# HttpCookieProcessor ----->Handler
# HttpHandler ProxyHandler
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)


# 使用handler创建Opener
opener = urllib.request.build_opener(cookie_handler)

# 豆瓣网页
# 登录POSRT
url = 'https://www.douban.com/accounts/login'
# form表单
'''
source=index_nav&form_email=18513106743&form_password=31415926abc'''

url_person = 'https://www.douban.com/people/164698173/'

# 全局安装，urllib.request.urlopen === 使用opener
urllib.request.install_opener(opener)

# 第一次请求登录获取cookier
params = {'source':'index_nav',
          'form_email':'18513106743',
          'form_password':'31415926abc'}

params = urllib.parse.urlencode(params).encode('utf-8')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

request = urllib.request.Request(url=url,data = params,headers=headers)

urllib.request.urlopen(request)

# 第二次获取个人主页,get请求
response = urllib.request.urlopen(url=url_person)


print(response.read().decode('utf-8'))

