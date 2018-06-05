import requests

# pip install lxml
from lxml import etree

import urllib
import urllib.request

# 使用关键字检索百度贴吧内容
url_base = 'http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%d'

# requests.get()


# 楼主详情界面
url_lz_base = 'http://tieba.baidu.com%s'


def downloadImage(img_urls):
    for url in img_urls:
        image_name = url.rsplit(sep = '/')[-1]

        urllib.request.urlretrieve(url=url,filename='./download/%s'%(image_name))
        print('下载图片%s成功'%(image_name))
    pass


def loadlzDetails(lzs):
    for lz in lzs:
        url_lz = url_lz_base % (lz)

        response = requests.get(url=url_lz,verify = False)

        response.encoding = 'utf-8'

        html = response.text

        html_tree = etree.HTML(html)

        #     获取楼主详情界面的图片
        '''<img class="BDE_Image" pic_type="0" width="560" height="372" 
        src="http://imgsrc.baidu.com/forum/w%3D580/sign=436043a8d5f9d72a17641015e42b282a/c0699c25bc315c606d844c7881b1cb13485477ae.jpg" 
        style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">'''
        img_urls = html_tree.xpath('//img[@class="BDE_Image"]/@src')

        # 下载图片
        downloadImage(img_urls)

    pass


def xpathParse(html):
    html_tree = etree.HTML(html)

    # lzs = html_tree.xpath('//li[contains(@class,"j_thread_list")]/div[@class="t_con cleafix"]/div/div/div/a/@href')
    lzs = html_tree.xpath('//div[contains(@class,"threadlist_title pull_left j_th_tit")]/a/@href')
    # print(len(lzs),lzs)

    # 加载楼主的详情界面
    loadlzDetails(lzs)

    pass


def loadtieba(key, page_start, page_end):
    headers = {'User-Agent': 'fjsl;jlfls'}
    for i in range(page_start, page_end + 1):
        url = url_base % (key, (i - 1) * 50)

        response = requests.get(url=url, headers=headers,verify = False)
        # response.encoding = 'utf-8'
        # 查看编码的方式
        print(response.encoding)

        html = response.text

        # 该方法，作用解析html数据，获取楼主的信息
        xpathParse(html)
    pass


if __name__ == '__main__':
    key = input('请输入搜索贴吧的关键字：')

    page_start = int(input('请输入贴吧的起始页：'))

    page_end = int(input('请输入贴吧的终止页：'))

    # 该方法加载贴吧的数据，各个楼主的数据
    loadtieba(key, page_start, page_end)
