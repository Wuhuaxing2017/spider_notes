import json

import jsonpath

# json 简单介绍
# JsonObject 格式{'key':value,'key2:value2} ------>python 对应的数据类型<class 'dict'>
# JsonArray 格式[]----->python 数据类型就是 <class 'list'>

data = ['item','item2','item3']
print(type(data))

j = json.dumps(data,ensure_ascii=False)
print(type(j))

zhilian = json.load(open('./zhilian.json','r',encoding='utf-8'))
print(zhilian)
print(type(zhilian))

# with open('./zhilian.json','r',encoding='utf-8') as fp:
#     content = fp.read()
#     print(content)
#     print(type(content))


# load /loads 可以将字符串------> python 类型的数据


# dump /dumps 可以将Python类型的数据列表，字典 ---------> 字符串 -------> 保存数据，写到文件中