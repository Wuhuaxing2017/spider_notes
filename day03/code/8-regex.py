import re

# 爬虫中，正则非常重要

# 整个获取一部分想要的数据

# 医生处方，道士的符，爬虫的正则


str = '234ab12 3tt;uh你好！UYT。HELLO'

# match ,匹配，从头开始，进行匹配，只匹配一个
# 查找字符串中的数据
# + 作用：匹配前一个字符一次多次
# * 作用：匹配前一个字符0次多次
patten = re.compile(r'\d*')

ret = patten.match(str)

# print(ret,ret.group())


# search 查找，查找整个字符串，也是匹配一个数据，进行返回
str = '234ab12 3tt;uh你好！UYT。HELLO'
pattern = re.compile(r'[a-z]+')

ret = pattern.search(str)

# print(ret,ret.group(),ret.span())



# findall 查询所有,返回的数据是列表
str = '234ab12 3tt;uh你好！UYT。HELLO'

pattern = re.compile(r'[a-zA-Z0-9]+')

ret = pattern.findall(str,pos=5,endpos=50)

# print(ret)

# finditer

iter = pattern.finditer(str,pos = 5,endpos=15)
# print(iter)

# 每一个item都是match对象
# for item in iter:
#     print(item.span(),item.group())


# split ，使用正则，将文本中所有的标点符号去除
# 返回的数据，列表的形式
str = '234ab12 3tt;uh你好！UYT。HELLO'
pattern = re.compile(r'[,;！\s 。]')

ret = pattern.split(str)
# print(ret)

str = '123 Hello; 456 World'

pattern = re.compile(r'(\w+) (\w+)')

ret = pattern.findall(str)

# print(pattern.sub(r'\2 \1',str))

# str 字符串中数字数据 ----> Cool
# map
def replace(item):
    return 'Cool ' + item.group(2)


# print(pattern.findall(str))
#
# # sub（参数一可以是一个方法）
# print(pattern.sub(replace,str))


# 批量修改这些数据，正则 Ctrl + R（replace）
# print('Hello')
# print('Hello')
# print('Hello')
# print('Hello')
# print('Hello')
# print('Hello')
# print('Hello')

# 匹配中文
str = '你好；23923sjlfjs；天气5678！@#%#Q%#@；骑士勇士大战'
pattern = re.compile(r'[\u4e00-\u9fa5]+')

print(pattern.findall(str))


# 贪婪模式非贪婪模式?
str = 'aa<div>test1</div>bb<div>test2</div>cc'

pattern = re.compile(r'<div>(.*)</div>')
print(pattern.findall(str))


# 添加？非贪婪模式，点到为止
pattern = re.compile(r'<div>(.*?)</div>')
print(pattern.findall(str))

