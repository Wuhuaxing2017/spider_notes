from selenium import webdriver

import json
import jsonpath

import re

browser = webdriver.Chrome()


# chrome有界面
# browser.get('https://www.qiushibaike.com/')
#
# span_list = browser.find_elements_by_xpath('//div[@class="content"]/span')
#
# for span in span_list:
#     content = span.text
#     print(content)
#
#
# browser.quit()

browser.get('https://www.lagou.com/lbs/getAllCitySearchLabels.json')


data = browser.page_source


pattern = re.compile('<body>(.*?)</body>')

print(pattern.findall(data))