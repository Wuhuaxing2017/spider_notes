import json

import jsonpath

import requests

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

response = requests.get(url = url,verify = False)
text = response.text

print(type(text))

print(text)


obj = json.loads(text)
print(type(obj))
print(obj)

# 获取字典中的name属性
print(obj['content']['data']['allCitySearchLabels']['A'][0]['name'])


# xpath  bs4 返回的数据批量

# json 批量获取数据 --------> jsonpath

# jsonpath 开头必须给$，$ 代表整个json对象
# cities = jsonpath.jsonpath(obj,'$..[name,id,code]')
content = jsonpath.jsonpath(obj,'$.content[data]')

print(content)
# print(cities)
# print(type(cities))