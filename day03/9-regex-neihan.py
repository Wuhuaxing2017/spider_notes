import requests
import re

url_first = 'http://www.neihan8.com/article/'
url = 'http://www.neihan8.com/article/index_%d.html/'

data = '''
<div class="text-column-item box box-790">
        <h3><a href="/article/209271.html" class="title" title="被一哥们儿的铃声雷到了">被一哥们儿的铃声雷到了</a></h3>
        <div class="desc"> 　　乘地铁遇到个牛人。　　地铁上，一哥们儿的铃声大作，众乘客一听： “爷爷，那孙子又给您来电话了&amp;hellip; 爷爷，那孙子又给您来电话了&amp;hellip; 爷爷，那孙子又给您来电话了。”　</div>
        <div class="bottom">
              <div class="time"><time class="timeago" datetime="2017-03-30.0">1年前</time><i>属于：<a href="/article/" class="title">内涵段子</a></i></div>
                <div class="good">38</div>
                <div class="bad">10</div>
                <div class="view">7036</div>             
            </div>
      </div>
'''

pattern = re.compile(r'<div class="desc>(.*?)</div>')


def write2file(items):
    with open('./download/内涵段子.txt', 'a')


def loadHtml(page):
    if page == 1:
        response = requests.get(url=url_first)
        r esponse.encoding = 'utf-8'
        html = response.text

        items = pattern.findall(html)
        write2file(items)

    elif page > 1:
        for p in range(1, page + 1):
            if p == 1:
                url_duanzi = url_first
            else:
                url_duanzi = url
    else:
        print("请输入整数！")
