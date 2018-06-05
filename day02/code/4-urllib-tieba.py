import urllib
import urllib.request
import urllib.parse

# 确定百度贴吧的url
# url关键数据是kw关键字，页码0（第一页） 50（第二页） 100，150
url = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%d'

key = input('请输入查询的贴吧关键字：')

page_start = input('请输入贴吧的起始页码：')

page_end = input('请输入贴吧的结束页码：')


kw =urllib.parse.quote(key)

# 转化页码

page_start = int(page_start)
page_end = int(page_end)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}


for i in range(page_start,page_end+1):

    # 创建url
    url_tieba = url%(kw,(i-1)*50)

    request = urllib.request.Request(url= url_tieba,headers=headers )

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    # 写入文件
    with open('./download/'+'第'+str(i)+'页.html','w',encoding='utf-8') as f:
        print('保存第'+str(i)+'页的数据成功')
        f.write(content)
