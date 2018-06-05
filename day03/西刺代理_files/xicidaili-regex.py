import re
import requests
import urllib
from urllib import request

data = '''
<tr class="">
    <td class="country"><img src="./西刺代理_files/cn.png" alt="Cn"></td>
    <td>180.118.241.94</td>
    <td>61234</td>
    <td>江苏镇江</td>
    <td class="country">高匿</td>
    <td>HTTP</td>
      <td>140天</td>
    <td>7分钟前</td>
  </tr>
'''

pattern = r'<tr class=.*?>.*?<td class.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*'
ip = re.findall(pattern,data)