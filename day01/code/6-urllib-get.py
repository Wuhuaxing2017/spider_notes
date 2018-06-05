import urllib
import urllib.request
import json
# ！！！ Get post
url = 'http://fanyi.baidu.com/sug?kw=%E8%8A%B1'


request = urllib.request.Request(url=url,headers={})

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
content_ = json.loads(content)
print(content_)