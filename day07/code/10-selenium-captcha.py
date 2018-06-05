# from captcha.image import ImageCaptcha
#
# from PIL import Image
#
# imageCaptcha = ImageCaptcha()
# img = imageCaptcha.generate_image('jfs4')
#
# img.show()
from selenium import webdriver
import time

url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

driver = webdriver.Chrome()

driver.get(url=url)
time.sleep(2)

driver.find_element_by_id('email').send_keys('455098435@qq.com')

driver.find_element_by_id('pwd').send_keys('31415926abc')


code = input('请输入验证码：')

driver.find_element_by_id('code').send_keys(code)

driver.find_element_by_id('denglu').click()

# 获取数据