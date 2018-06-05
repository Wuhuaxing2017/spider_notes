import requests

from bs4 import BeautifulSoup

# url 是网页，如果是json数据一般情况下，可以修改参数控制返回的条目
url_base = 'https://hr.tencent.com/position.php?keywords=Python&start=%d'


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
def loadhtml(start_page):
    url = url_base % (start_page * 10)

    response = requests.get(url=url, verify=False,headers = headers)
    print(response.encoding)
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    # print(soup)

    even = soup.find_all('tr', attrs={'class': 'even'})
    odd = soup.find_all('tr', attrs={'class': 'odd'})

    print(len(even),len(odd))

    for e in even:
        # print(e)
        info = e.select('td')
        # print(info)
        job = info[0].select('a')[0].string
        type = info[1].string
        num = info[2].string
        address = info[3].string
        date = info[4].string
        print(job,address,date)
'''<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=40827&amp;keywords=Python&amp;tid=0&amp;lid=0">16175-游戏测试工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-06-01</td>
		    	</tr>'''

if __name__ == '__main__':
    start_page = int(input('请输入起始页'))

    loadhtml(start_page)
