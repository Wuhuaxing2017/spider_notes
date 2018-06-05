import urllib
from urllib import request,parse

url = 'http://fanyi.baidu.com/v2transapi'
word = input('请输入要翻译的文字：')

from = {
	'from':'zh',
	'to':'en',
	'query':word,
	'transtype':''
}