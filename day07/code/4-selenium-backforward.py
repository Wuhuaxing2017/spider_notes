from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('http://www.baidu.com/')


browser.find_element_by_id('kw').send_keys('骑士')

browser.find_element_by_id('su').click()

time.sleep(5)

# 后退
browser.back()

browser.save_screenshot('./download/baidu_back.png')

time.sleep(5)
# 前进
browser.forward()
browser.save_screenshot('./download/baidu_forward.png')

input('点击Enter退出：')

browser.quit()