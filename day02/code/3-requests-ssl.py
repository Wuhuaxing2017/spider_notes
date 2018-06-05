import requests


'''Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')],)",),))
'''
url = 'https://www.12306.cn/mormhweb/'

# requests操作起来简单
response = requests.get(url=url,verify = False)

response.encoding = 'utf-8'

print(response.text)