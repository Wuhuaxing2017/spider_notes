import urllib
import urllib.request

# 导包ssl
import ssl

# 对，ssl进行设置，忽略警告，继续进行访问
ssl._create_default_https_context = ssl._create_unverified_context

'''ssl.CertificateError: hostname 'www.12306.cn' doesn't match either of 'webssl.chinanetcenter.com','''
url = 'https://www.12306.cn/mormhweb/'


response = urllib.request.urlopen(url=url)

print(response.read().decode('utf-8'))