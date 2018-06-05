import re

import requests
import urllib
import urllib.request


data = ''' <tr class="odd">
    <td class="country"><img src="./西刺代理_files/cn.png" alt="Cn"></td>
    <td>118.81.70.49</td>
    <td>9797</td>
    <td>山西太原</td>
    <td class="country">透明</td>
    <td>HTTPS</td>
      <td>4小时</td>
    <td>6分钟前</td>
  </tr>'''


'''.*?      ="country"><img src="./西刺代理_files/cn.png" alt="Cn">'''
pattern = r'<tr class=.*?>.*?<td class.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*'
# #
# ip = re.findall(pattern,data,re.S)
#
# print(ip)

pattern = r'<td>([\d \. A-Za-z\/]+)</td>'


pattern = r'<td>([\d\.HTTPHTTPSsocks4/5]+)</td>'
# # pattern = r'<td>([\w]+)</td>'
# # ips = re.findall(pattern,data)
# #
# # print(ips)
#
with open('./西刺代理.html','r',encoding='utf-8') as fp:
    data = fp.read()

ips = re.findall(pattern,data,re.S)
#
# # str = 'aabb  33hh,ni你好，bbuu，235'
# #
# # p = r'\w+'
print(ips)
print(len(ips))
# # print(re.findall(p,str))


str = 'HTTP TTPH;PPTH'

p = r'[HTTP ]+'

print(re.findall(p,str))