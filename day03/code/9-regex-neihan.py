import requests

import re

url_first = 'http://www.neihan8.com/article/'

# 网址特殊，后缀是.html -----> 文件到头
# !!! 后缀不能加：/
url = 'http://www.neihan8.com/article/index_%d.html'


print(url%(10))

data = '''<div class="text-column-item box box-790">
        <h3><a href="/article/209047.html" class="title" title="人流你都不怕">人流你都不怕</a></h3>
        <div class="desc"> 　　最近这几天感冒了。早上去坐公交，忍不住打了个喷嚏&amp;hellip;&amp;hellip;　　只听一个女的娇滴滴地说：“老公，听说最近甲流很流行，被传染了怎么办?”　　只听旁边的壮汉冷冷地说</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2017-03-29.0">1年前</time><i>属于：<a href="/article/" class="title">内涵段子</a></i></div>
                <div class="good">0</div>
                <div class="bad">2</div>
                <div class="view">1679</div>             
            </div>
      </div>'''

pattern = re.compile(r'<div class="desc">(.*?)</div>')

# ret = pattern.findall(data)
# print(ret)

def write2file(items):
    with open('./download/内涵段子.txt','a',encoding='utf-8') as fp:
        print('---------------------',len(items))
        for item in items:
            fp.write(item+'\n')
            fp.write('---------------------------------------------------------------\n')
    pass


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

def loadHtml(page):

    if page == 1:

        response = requests.get(url=url_first,headers = headers)
        response.encoding = 'utf-8'
        html = response.text

        # 列表
        items = pattern.findall(html)

        write2file(items)
        pass
    elif page > 1:

        for p in range(1,page+1):
            if p == 1:
                url_duanzi = url_first
            else:
                url_duanzi = url%(p)

            print(url_duanzi)

            response = requests.get(url=url_duanzi,headers = headers)

            response.encoding = 'utf-8'

            content = response.text

            # Ctrl + Alt + V:提取变量
            items = pattern.findall(content)

            write2file(items)
        pass
    else:
        print('请输入数字！！！')
    pass


if __name__ == '__main__':
    page = int(input('请输入爬取多少页：'))

    loadHtml(page)