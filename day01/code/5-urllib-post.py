import urllib
import urllib.request
import urllib.parse
import json

url = 'http://fanyi.baidu.com/sug'

key = input('请输入翻译的汉字：')
# k = urllib.parse.quote(key)

params = {'kw':key}
print(params)
params = urllib.parse.urlencode(params).encode('utf-8')
print(params)

response = urllib.request.urlopen(url= url,data=params)

content = response.read().decode('utf-8')

content_ = json.loads(content)

print(content,content_)