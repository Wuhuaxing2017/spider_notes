import urllib
import urllib.request


url = 'http://www.qq.com/'

# 构造request发送请求
# 可以通过Request模仿浏览器


# 最初级的伪装，伪装成浏览器获取爬虫的数据
# 网络获取的数据，很多gzip，decode 会出问题，通过请求头的中字段'Accept-Encoding':''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
           'Connection':'keep-alive',
           'Accept-Encoding':'',
           'Cookie':'RK=wDlaxzBPH0; pgv_pvi=6715893760; pac_uid=1_455098435; ts_uid=6068238491; tvfe_boss_uuid=4c1c1d356336c0db; h_uid=h579981304587140570; ptcz=1d7f9c4f7f744f24708b98a6772f5bb15a37065035b433e620e6a706873cca40; pt2gguin=o0455098435; pgv_pvid=5482877460; o_cookie=455098435; pgv_info=ssid=s3763149018; ts_last=www.qq.com/; ad_play_index=35; qv_als=9NavEztTkd2+WaXGA11527494086cKMoxQ=='
           }

# 请求
request = urllib.request.Request(url=url,headers=headers)

# 发起请求
response = urllib.request.urlopen(request)

print(response.read().decode('gbk'))