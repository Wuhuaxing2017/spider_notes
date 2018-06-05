import requests

# 对于urllib 验证需要
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# 豆瓣
url = 'https://www.douban.com/accounts/login'
# form表单
'''
source=index_nav&form_email=18513106743&form_password=31415926abc'''

url_person = 'https://www.douban.com/people/164698173/'

# 第一次请求登录获取cookier
params = {'source':'index_nav',
          'form_email':'18513106743',
          'form_password':'31415926abc'}

# 会话在自己生命周期之内，多次进行网络请求，自动记录cookie
session = requests.Session()

# 第一步请求，登录
# 对于requests 模块，不需要urlencode
session.post(url=url,data=params,verify = False)


# 第二步，获取豆瓣，个人主页信息
response = session.get(url=url_person,verify = False)

response.encoding = 'utf-8'

print(response.text)