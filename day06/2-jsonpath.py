import json

import jsonpath

# JsonObject是一个字典格式
# JsonArray []

data = ['item','item2','item3']
print(type(data))
j = json.dumps(data,ensure_ascii=False)
print(type(j))

json.load(open('./zhilian.json','r',encoding='utf-8'))

with open('./zhilian.json','r',encoding='utf-8') as fp:
	content = fp.read()

# https://www.lagou.com/lbs/getAllCitySearchLabels.json