from selenium import webdriver
import  time

browser = webdriver.Chrome()

# browser.get('https://music.douban.com/')
#
#
#
# # 滑动到页面的最底部
# # js = 'document.documentElement.scrollTop=10000'
#
# js = 'document.documentElement.scrollTop=document.body.scrollHeight'
#
# browser.execute_script(js)
#
# input('回车键退出程序：')

browser.get('http://www.baidu.com/')



img = browser.find_element_by_class_name('index-logo-src')

print(img)

browser.execute_script("$(arguments[0]).fadeOut()",img)

#
browser.execute_script("var q = document.getElementById(\"kw\");q.style.border=\"2px solid red\"")

input('点击回车键退出程序：')

browser.quit()