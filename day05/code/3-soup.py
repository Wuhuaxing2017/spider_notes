from bs4 import BeautifulSoup

import bs4

import re

# xpath 下载数据 ------> etree.HTML(html_tree)------------>xpath('//')

# 解析xml html类型的数据
# 速度慢一些，简单
# 正则 < xpath < soup(花费时间)
# 正则 > xpath > soup(难度)

data = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>soup测试</title>
    <title class="warm">你那温情的一笑，搞得我瑟瑟发抖</title>
</head>
<body>
<div class="tang">
    <ul>
        <li class="hello" id="world"><a href="http://www.baidu.com" title="出塞"><!--秦时明月汉时关，万里长征人未还，但使龙城飞将在，不教胡马度阴山--></a></li>
        <list><a href="https://www.baidu.com" title="出塞" style="font-weight: bold"><!--秦时明月汉时关，万里长征人未还，但使龙城飞将在，不教胡马度阴山--></a></list>
        <li><a href="http://www.163.com" class="taohua" title="huahua">人面不知何处去，桃花依旧笑春风</a></li>
        <lists class="hello"><a href="http://mi.com" id="hong" title="huahua">去年今日此门中，人面桃花相映红</a></lists>
        <li id="wo"><a href="http://qq.com" name="he" id="gu">故人西辞黄鹤楼，烟花三月下扬州</a></li>
    </ul>
    <ul>
        <li class="hello" id="sf"><a href="http://www.baidu.com" title="出塞"><!--秦时明月汉时关，万里长征人未还，但使龙城飞将在，不教胡马度阴山--></a></li>
        <list><a href="https://www.baidu.com" title="出塞"><!--秦时明月汉时关，万里长征人未还，但使龙城飞将在，不教胡马度阴山--></a></list>
        <li><a href="http://www.163.com" class="taohua">人面不知何处去，桃花依旧笑春风</a></li>
        <lists class="hello"><a href="http://mi.com" id="fhsf">去年今日此门中，人面桃花相映红，不知桃花何处去，出门依旧笑楚风</a></lists>
        <li id="fs"><a href="http://qq.com" name="he" id="gufds">故人西辞黄鹤楼，烟花三月下扬州</a></li>
    </ul>
</div>
<div id="meng">
    <p class="jiang">
        <span>三国猛将</span>
    <ol>
        <li>关羽</li>
        <li>张飞</li>
        <li>赵云</li>
        <li>马超</li>
        <li>黄忠</li>
    </ol>
    <div class="cao">
        <ul>
            <li>典韦</li>
            <li>许褚</li>
            <li>张辽</li>
            <li>张郃</li>
            <li>于禁</li>
            <li>夏侯惇</li>
        </ul>
    </div>
    </p>
</div>
</body>
</html>'''

# soup = BeautifulSoup(data,'lxml')

soup = BeautifulSoup(open('./soup.html',mode = 'r',encoding= 'utf-8'),'lxml')

# 第一类对象:BeautifulSoup
# print(soup)
# print(type(soup))

# 第二类标签 Tag
# 只会返回第一个标签
t = soup.li
# print(t)
# print(type(t))


# 第三类数据类型NavigableString
t = soup.span.string
# print(t)
# print(type(t))


# 第四种，Comment，注释
# t = soup.li.string
# print(t)
# print(type(t) == bs4.Comment)

# 遍历
children = soup.div.ul.children
# print(children)
# for c in children:
#     print(c)

# des = soup.div.ul.descendants
des = soup.div.ul.contents
# for d in des:
#     print(d)

div = soup.find(name = 'div',attrs = {'id':'meng'})
# print(div)

li = soup.find(name = 'head')
# print(li)

# soup 返回数据都是列表的形式

li = soup.find_all('a',title = re.compile(r'.*'))
# li = soup.find_all('a',title = '出塞')
#
# print(li)
# print(len(li))


# soup 中查询数据使用css表达式
# 标签直接写  id-----># 类名------->.
# soup.select(css 表达式)
# li > a
# find_all方法
s = soup.select('div#meng')

# print(s,len(s))
s = soup.select('div.tang')
# print(s)

# 使用逗号，间隔，表示查询多个
# 属性id class
# 属性 href title……

# soup 最后一点：contains，语法,不支持，
# 属性查找a[属性]
s = soup.select('a[title="出塞"]')
print(s)
print(len(s))