import requests

# lxml
# element 标签
# etree 标签树
from lxml import etree

url =  'https://www.qiushibaike.com/text/'

x = '''/html/body/div[@id='content']/div[@class='content-block clearfix']/div[@id='content-left']/div[@id='qiushi_tag_120441381']/div[@class='author clearfix']/a[1]/img/@src'''


x = '''/html/body/div[@id='content']/div[@class='content-block clearfix']/div[@id='content-left']/div[@id='qiushi_tag_112124634']/div[@class='author clearfix']/a[1]/img/@src'''

x = '//img/@src'

x = '''/html/body/div[@id='content']/div[@class='content-block clearfix']/div[@id='content-left']
/div[@id='qiushi_tag_112124634']/a[@class='contentHerf']/div[@class='content']/span'''

x = '//div[@class="content"]/span/text()'
response = requests.get(url=url,verify = False)
response.encoding = 'utf-8'

# String 串
html = response.text

# 使用etree，转换成标签树
# json.loads() 类似


html_tree = etree.HTML(html)

# print(html_tree)
# print(etree.tostring(html_tree).decode('utf-8'))


# 对etree对象使用xpath方法，根据xpath语句进行数据的查找
src = html_tree.xpath(x)

print(src)