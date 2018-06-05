import requests
from lxml import etree
import urllib
import urllib.request
import os
url = 'http://sc.chinaz.com/tupian/shamotupian.html'

x = '''/html/body/div[@class='all_wrap']/div[@class='index_only']
/div[@class='left pic_left_l']/div[@class='text_left text_lefts']/div[@id='container']
/div[@class='box picblock col3 masonry-brick'][1]/div/a/img/@src'''


data = '''<div class="box picblock col3 masonry-brick" style="width: 186px; height: 156px; position: absolute; top: 0px; left: 0px;">
                    <div>
                    <a target="_blank" href="http://sc.chinaz.com/tupian/180531579563.htm" alt="新疆沙漠风景图片"><img alt="新疆沙漠风景图片" 
                    src="http://pic2.sc.chinaz.com/Files/pic/pic9/201805/wpic982_s.jpg"></a>
                    </div>
                    <p><a target="_blank" href="http://sc.chinaz.com/tupian/180531579563.htm" alt="新疆沙漠风景图片">新疆沙漠风景图片</a></p>
                    </div>'''

# requests获取的数据：
data = '''<div class="box picblock col3" style="width:186px;height:311px">
                    <div>
                    <a target="_blank" href="http://sc.chinaz.com/tupian/180316401614.htm" alt="西北地区荒漠化图片"><img 
                    src2="http://pic2.sc.chinaz.com/Files/pic/pic9/201803/wpic011_s.jpg" alt="西北地区荒漠化图片"></a>
                    </div>
                    <p><a target="_blank" href="http://sc.chinaz.com/tupian/180316401614.htm" alt="西北地区荒漠化图片">西北地区荒漠化图片</a></p>
                    </div>'''


# 第二步，修改xpath语句
x = '//div[@class="box picblock col3"]/div/a/img/@src2'

# html_tree = etree.HTML(data)
#
# src = html_tree.xpath(x)
#
# print(src)
response = requests.get(url=url)

response.encoding = 'utf-8'

# 调用属性就可以了
html = response.text

# 解决问题第一步
# print(html)

html_etree = etree.HTML(html)

src = html_etree.xpath(x)

print(src)


# http://pic2.sc.chinaz.com/Files/pic/pic9/201805/wpic982_s.jpg

for img_url in src:
    
    img_name = os.path.split(img_url)[-1]

    urllib.request.urlretrieve(img_url,filename='./images/%s'%(img_name))

    print('下载图片%s成功！'%(img_name))