import urllib
import urllib.request

url = 'http://www.baidu.com/'
headers = {'User-Agent':''}

response = urllib.request.urlopen(url = url,headers = headers)
print(response.read().decode('utf-8'))