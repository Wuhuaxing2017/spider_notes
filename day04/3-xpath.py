import requests
from xml import etree

url = 'https://www.qiushibaike.com/text/'

x = '''
/html/body/div[@id='content']/div[@class='content-block clearfix']/div[@id='content-left']/div[@id='qiushi_tag_120492939']/div[@class='thumb']/a/img/@src
'''
response = requests.get(url=url,verify = False)
response.encoding = 'utf-8'

html = response.text
html_tree = etree.HTML(html)
print(html_tree)
pritn(etree.tosring(html_tree).decode('utg-8'))

a = etree.H