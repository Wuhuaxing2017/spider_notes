import requests

# 	47.92.91.40	16817
# 455098435密码：lbrv3bgb


# requests 私密代理格式：http：//username:password@ip:port
proxies = {'http':'http://455098435:lbrv3bgb@47.92.91.40:16817'}

reposne = requests.get(url='http://www.xicidaili.com/',proxies = proxies)

reposne.encoding = 'utf-8'

print(reposne.text)