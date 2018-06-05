import requests
from lxml import etree

url = 'https://www.qiushibaike.com/text/'

x = '''/html/body/div[@id='content']/div[@class='content-block clearfix']/div[@id='content-left']/div[@id='qiushi_tag_120491025']/div[@class='author clearfix']/a[1]/img/@src'''

x = '''/html/body/div[@id='content']/div[@class='content-block clearfix']/div[@id='content-left']/div[@id='qiushi_tag_120441381']/a[@class='contentHerf']/div[@class='content']/span'''

response = requests.get(url=url,verify = False)
response.encoding = 'utf-8'

html  =response.text
html_tree = etree.HTML(html)

div = html_tree.xpath(x)
# print(etree.tostring(div[0]))
print(div[0])