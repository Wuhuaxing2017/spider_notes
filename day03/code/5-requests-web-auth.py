import requests

user = 'admin'
password = '123456'

url = 'http://10.11.58.219/'

# requests对于web验证auth
# auth 参数 给元组（username，password）
# urllib泪奔
# request 来自与urllib3
reponse = requests.get(url=url,auth =(user,password))
reponse.encoding = 'utf-8'

print(reponse.text)