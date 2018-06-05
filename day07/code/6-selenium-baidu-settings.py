from selenium import webdriver

import time

browser = webdriver.Chrome()

browser.get('http://www.baidu.com/')
time.sleep(1)


setting = browser.find_element_by_link_text('设置')

setting.click()

browser.find_element_by_link_text('搜索设置').click()

time.sleep(1)

browser.find_elements_by_xpath('//option')[2].click()

browser.find_element_by_class_name('prefpanelgo').click()


time.sleep(1)

# 处理alert
browser.switch_to.alert.accept()

browser.find_element_by_id('kw').send_keys('美女')

browser.find_element_by_id('su').click()

time.sleep(10)

browser.quit()