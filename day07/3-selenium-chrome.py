from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://www.qiushibaike.com/")
span_list = browser.find_element_by_xpath('//div[@class="content"]/span')

for span in span_list:
	content = span.text
	print(content)

browser.quit()