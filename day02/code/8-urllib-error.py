import urllib
import urllib.request

url = 'http://www.abcdefydflsjlf.com/'

# 捕获异常，为了让程序健壮
# 爬虫，批量获取数据，url 0 ~ 100 其中某一页，数据崩溃了，
try:
    response = urllib.request.urlopen(url=url)
    print(response.read().decode('utf-8'))
except Exception as err:
    print(err)


