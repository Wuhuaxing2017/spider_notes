import requests

import re
import urllib
import urllib.request



url_first = 'https://www.qiushibaike.com/pic/'

url = 'https://www.qiushibaike.com/pic/page/%d/'

data = '''<div class="thumb">

<a href="/article/120491686" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12049/120491686/medium/app120491686.jpg" alt="你是不是太激动了">
</a>

</div>'''


def downloadImage(imgs):

    for img_url in imgs:
        fileName = img_url.rsplit(sep='/',maxsplit=1)[-1]

        urllib.request.urlretrieve('http:'+img_url,'./download/%s'%(fileName))

        print('图片：%s下载成功！'%(fileName))

    pass


def parseHtml(html):
    # re.S 作用忽略换行，将所有的数据作为整体，进行匹配
    pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?</div>',re.S)

    imgs = pattern.findall(html)

    # 下载图片
    downloadImage(imgs)
    pass


def loadhtml(page):

    if page == 1:
        url_html = url_first
        # 请求中，需要添加请求头
        response = requests.get(url_html)

        response.encoding = 'utf-8'

        html = response.text

        # 使用正则，解析html页面的图片url
        parseHtml(html)
    else:
        for i in range(1,page+1):
            if i == 1:
                url_html = url_first
            else:
                url_html = url%(i)
            response = requests.get(url_html)
            response.encoding = 'utf-8'
            html = response.text
            parseHtml(html)
            time.sleep(60)
        pass


    pass


# http://pic.qiushibaike.com/system/pictures/12049/120491816/medium/app120491816.jpeg

# ！！！ 批量爬去数据的时候，time sleep 程序休眠一定时间，再去爬去服务器的数据
import time

time.sleep(60)

if __name__ == '__main__':
    page = int(input('请输入爬去图片的页数：'))
    
    loadhtml(page)

    # pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?</div>', re.S)
    #
    # print(pattern.findall(data))
    #
    # url = '//pic.qiushibaike.com/system/pictures/12049/120491686/medium/app120491686.jpg'
    #
    # print(url.rsplit('/',maxsplit=1)[-1])