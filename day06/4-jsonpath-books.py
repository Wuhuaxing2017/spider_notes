import json
import jsonpath

obj = json.load(open('./books.json','r',encoding='utf-8'))

books = jsonpath.jsonpath(obj,'$.store.book')
print(books)

jsonpath.jsonpath(obj,'$..book[1]') 0