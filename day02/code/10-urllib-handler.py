import urllib
import urllib.request


handler = urllib.request.HTTPHandler()

# urlopen
# opener作用，打开url
# opener == urllib.request
opener = urllib.request.build_opener(handler)

url = 'http://www.qq.com/'

# urllib.request.urlopen()

request = urllib.request.Request(url=url,headers={'Accept-Encoding':''})

response = opener.open(request)

print(response.read().decode('gbk'))