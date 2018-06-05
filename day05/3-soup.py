from bs4 import BeautifulSoup

# 正则>xpath>soup

data = '''

'''

soup = BeautifulSoup(open('./soup.html',mode = 'r',encoding = 'utf-8'),'lxml')

children = soup.div.ul.children

des = soup.div.ul.contents

div = soup.find(name = 'div',attrs = {'id':'meng'})
li = soup.find(name = ['div','head'])
print(li)