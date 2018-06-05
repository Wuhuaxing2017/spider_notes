import json
import jsonpath

# JsonObject  ----> python -------> dict
obj  = json.load(open('./books.json','r',encoding='utf-8'))

# $ 代表这整个json对象
# books = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(books)


# ret = jsonpath.jsonpath(obj,'$..author')
# print(ret)
#
# # @ 代表当前数据对象
# ret = jsonpath.jsonpath(obj,'$..book[(@.length - 4)]')
#
# print(ret)
#
#
# ret = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# print(ret)

ret = jsonpath.jsonpath(obj,'$..book[?(@.price < 10)]')
print(ret)