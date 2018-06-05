import urllib

import urllib.request

# ！！！爬虫时候，url最后+/
url = 'http://www.qq.com/'

response = urllib.request.urlopen(url = url)

# 打印response中的数据
content = response.read().decode('gbk')

print(content)