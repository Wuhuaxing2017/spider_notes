from lxml import etree

html = '''<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html" class="linkjfdlsfjls">third item</a></li>
         <li class="shfs-inactive"><a href="link4.html">third item</a></li>
         <li class="isjfls-inactive"><a href="link5.html">third item</a></li>
         <li class="qwert-inactive"><a href="link6.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>'''

# 数据转换成标签树方式一
html_tree = etree.HTML(html)

# 方式二，可以将文件中的直接进行转换
html_tree2 = etree.parse('./data.html')

# print(html_tree,html_tree2)

# print(etree.tostring(html_tree).decode('utf-8'))
# 获取文件中所有的标签li
# xpath返回的数据是列表,标签<Element 内存地址>
li = html_tree.xpath('//li')
# print(li)


li = html_tree.xpath('//li[@class="item-1"]')
# print(li[0].xpath('..//a/text()'))


# 查询class属性不等于“item-1” 标签
li = html_tree.xpath('//li[@class!="item-1"]')
# print(li)


# 查询li标签，class 包含inactive 字符串
li = html_tree.xpath('//li[contains(@class,"inactive")]')
# print(li)
# print(li[0].xpath('./a/@*'))


# 查询li标签，class 不包含inactive字符串
li = html_tree.xpath('//li[not(contains(@class,"inactive"))]')
# print(li)
# print(etree.tostring(li[0]).decode('utf-8'))


# 查询li标签，class 不包含inactive字符串 同时包含class =item-1
li = html_tree.xpath('//li[not(contains(@class,"inactive"))][@class="item-1"]')
# print(li)
# print(etree.tostring(li[-1]).decode('utf-8'))


# 查询li标签，最后一个
# print(etree.tostring(html_tree).decode('utf-8'))
li = html_tree.xpath('/html/body/div/ul/li')
li = html_tree.xpath('//li[last()-1]')
# print(li,etree.tostring(li[0]))


# 查询位置小于4的标签
li = html_tree.xpath('//li[position()<4]')
print(li)
