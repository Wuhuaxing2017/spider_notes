import urllib
from urllib import request,response


url = 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3862787450,1536923084&fm=27&gp=0.jpg'

# 保存文件
url_video = 'http://vf1.mtime.cn/Video/2015/03/20/mp4/150320094140850937_480.mp4'


urllib.request.urlretrieve(url = url_video,filename='./video.mp4')
 