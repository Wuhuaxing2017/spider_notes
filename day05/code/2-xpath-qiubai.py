import requests

from lxml import etree

import time

import random

import json

url_base = 'https://www.qiushibaike.com/text/page/%d/'


def write2file(items):
    print(len(items))
    with open('./糗事百科.json','w',encoding='utf-8') as fp:

        # replace.('\n','')
        fp.write(json.dumps(items,ensure_ascii=False))

    pass


def loadqiubaihtml(page):
    count = 0
    # 段子的信息，列表，字典
    items = []
    for p in range(1,page+1):

        try:
            url = url_base%(p)

            response = requests.get(url=url,timeout = 5000,verify = False)
            response.encoding = 'utf-8'
            html = response.text
            html_tree = etree.HTML(html)

            # 每一页页面有很多段子，获取多个段子
            duanzi_list = html_tree.xpath('//div[@class="article block untagged mb15 typs_hot"][contains(@id,"qiushi_tag")]')

            print(len(duanzi_list))

            for dz in duanzi_list:
                #     作者，内容，评论，好笑
                author = dz.xpath('.//h2/text()')[0]
                content = dz.xpath('.//div[@class="content"]/span')[0].text
                vote = dz.xpath('.//div[@class="stats"]/span[@class="stats-vote"]/i/text()')[0]
                comments = dz.xpath('.//div[@class="stats"]/span[@class="stats-comments"]/a/i/text()')[0]
                item = {}
                item['author'] = author
                item['content'] = content
                item['vote'] = vote
                item['comments'] = comments
                items.append(item)
            # 多个段子中获取内容，作者，评论等信息
            t = random.randint(10,20)
            time.sleep(t)
            pass
        except Exception as e:
            print(e)
            count += 1
            if count > 3:
                break

    write2file(items)
    pass

if __name__ == '__main__':
    while True:
        try:
            page = int(input('请输入爬去页数：'))

            if page < 0:
                print('请输入正整数：')
            else:
                break
        except Exception as e:
            print('请输入数字：')
    loadqiubaihtml(page)
