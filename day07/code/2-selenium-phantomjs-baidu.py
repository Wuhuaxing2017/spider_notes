from selenium import webdriver
import time

# 启动无界面的浏览器
browser = webdriver.PhantomJS()


# 网址
browser.get('http://www.baidu.com/')


# 百度首页的文本输入框的id是：kw
browser.find_element_by_id('kw').send_keys('美女')


time.sleep(2)

# 百度首页找到“百度一下”button按钮
btn = browser.find_element_by_xpath('//input[@id="su"]')

print(btn)

btn.click()

time.sleep(1)

# 保存一下虚拟浏览器页面
browser.save_screenshot('./download/baidu.png')


input('点击任意键程序退出：')

# 程序退出
browser.quit()