import requests
import re

import urllib
import urllib.request

url_formhash = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes'

# 使用get请求获取url_formhash 这个界面html数据有关键的字段 input name = formhash ------> value

print('hello')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

html = requests.get(url=url_formhash,headers = headers).text
# response = urllib.request.urlopen(url=url_formhash)
#
# html = response.read().decode('utf-8')
print('hello------')
# <input type="hidden" name="formhash" value="e40c5879" />
pattern = re.compile('<input type="hidden" name="formhash" value="(.*?)" />')

formhash = pattern.findall(html)[0]


url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LBEpA'

'''
formhash=968ddc7a
&referer=http%3A%2F%2Fbbs.chinaunix.net%2F
&username=18513106743
&password=31415926abc
&loginsubmit=true
&return_type='''

# 这个网站对于参数要求不严
form = {'formhash':formhash,
        'referer':'http%3A%2F%2Fbbs.chinaunix.net%2F',
        'username':'18513106743',
        'password':'31415926abc',
        'loginsubmit':'true',
        'return_type':''}


response = requests.post(url = url,data = form,headers = headers)

print(response.text)

print(formhash)