import requests

# 117.90.7.88	9000

# 相对来说，简单很多
proxies = {'http':'123.57.217.208:3128'}
response = requests.get(url='http://www.baidu.com/',proxies = proxies)

response.encoding = 'utf-8'

print(response.text)