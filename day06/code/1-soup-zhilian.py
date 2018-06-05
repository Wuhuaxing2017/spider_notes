import requests

from bs4 import BeautifulSoup

import json

url_base = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&p=%d'


class Zhilian(object):


    # Ctrl + o overwrite
    def __init__(self,url_base,city,job,page) -> None:
        super().__init__()
        self.url = url_base
        self.city = city
        self.job = job
        self.page = page
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
        self.items = []

    # 爬虫启动
    def start(self):
        for i in range(1,self.page+1):
            url = self.url%(self.city,self.job,i)

            # 网络获取数据
            html = self.handle_url(url)

        #     使用soup对数据进行解析
            self.soup_parse(html)

        # 将数据持久化存储
        self.write2file(self.items)
        pass

    def handle_url(self, url):
        response = requests.get(url=url,headers = self.headers,verify = False)

        return response.text

    def soup_parse(self, html):

        soup = BeautifulSoup(html,'lxml')

        # 从soup对象中获取数据，每一个工作行
        tables = soup.select('div.newlist_list_content > table')[1:]

        for table in tables:
            company = table.select('td.gsmc > a')[0].string
            salary = table.select('td.zwyx')[0].get_text()
            location = table.select('td.gzdd')[0].string
            work = table.select('td.zwmc > div > a')[0].get_text()

            item = {}
            item['company'] = company
            item['salary'] = salary
            item['location'] = location
            item['work'] = work

            # 数据保存到成员属性，items中
            self.items.append(item)

    def write2file(self, items):

        # 输出保存
        json.dump(items,open('./zhilian.json','w',encoding='utf-8'),ensure_ascii=False)




if __name__ == '__main__':
    city = input('请输入查询城市：')
    job = input('请输入查询的工作：')

    # try except
    page = int(input('请输入查询的页码数量：'))

#     现在用类封装所有的方法
    zhilian = Zhilian(url_base,city,job,page)

#     调用对象中方法
    zhilian.start()


