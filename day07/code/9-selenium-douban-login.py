from selenium import webdriver
import time
from PIL import Image
url = 'https://www.douban.com/accounts/login?source=music'

driver = webdriver.Chrome()


driver.get(url=url)
time.sleep(1)


driver.find_element_by_id('email').send_keys('18513106743')

driver.find_element_by_id('password').send_keys('31415926abc')


# 假设有验证码，标签-------图片url

# 网络请求获取图片 图片保存本地，然后使用Image显示

verify = input('请输入验证码：')



driver.find_element_by_name('login').click()

input('Enter 退出')

driver.quit()