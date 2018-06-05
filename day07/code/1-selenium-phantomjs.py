from selenium import webdriver
import time

# 相当于浏览器
path = r"C:\phantomjs-2.1.1-windows\bin\phantomjs.exe"
browser = webdriver.PhantomJS()

# 向浏览器中添加请求
browser.get('https://movie.douban.com/chart')

time.sleep(5)


html = browser.page_source
with open('./douban.html','w',encoding='utf-8') as fp:
    fp.write(html)
    print('数据写到文件成功')