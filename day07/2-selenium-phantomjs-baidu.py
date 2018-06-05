from selenium import webdriver
import time

browser = webdriver.PhantomJS()

browser.get('http://www.baidu.com/')

# 百度首页文本框输入id

btn = browser.find_element_by_id('kw').send_keys('雷军')
# 寻找“百度一下”按钮
browser.find_element_by_xpath('//span[@id="s_btn_wr"]/input').click()
time.sleep(5)

# 保存一下虚拟浏览器页面
browser.save_screenshot('./download/baidu.png')



input('点击任意键退出：')
# 程序退出
browser.quit()