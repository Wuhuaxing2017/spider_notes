import re

str = '210ab 213;un您好!UTY。hello'

# match 从头开始匹配，只匹配一个
patten = re.compile(r'\d+')
ret = patten.match(str)

# print(ret,ret.group())
