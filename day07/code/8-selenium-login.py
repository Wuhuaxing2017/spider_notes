from selenium import webdriver
import time
driver = webdriver.Chrome()

# post url
url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&logsubmit=yes'

driver.get(url=url)

time.sleep(2)

driver.find_element_by_name('username').send_keys('18513106743')

driver.find_element_by_name('password').send_keys('31415926abc')

time.sleep(1)

driver.find_element_by_name('loginsubmit').click()

time.sleep(5)

with open('./download/chinaunix.html','w',encoding='utf-8') as fp:
    fp.write(driver.page_source)

time.sleep(20)

driver.quit()

