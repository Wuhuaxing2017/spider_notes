import urllib
import urllib.request
import urllib.parse

# windows7系统同学，访问https，都需要添加ssl认证
import  ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

'''
cname=%E4%B8%8A%E6%B5%B7&pid=&pageIndex=1&pageSize=10'''

city = input('请输入查询的城市：')
page = int(input('请输入查询的页码：'))

form = {'cname':city,
        'pid':'',
        'pageIndex':page,
        'pageSize':'10'}

params = urllib.parse.urlencode(form).encode('utf-8')

request = urllib.request.Request(url= url,data = params)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))