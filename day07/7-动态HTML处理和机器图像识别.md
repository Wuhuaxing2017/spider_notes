# 动态HTML处理和机器图像识别

### 一、爬虫建议

- 尽量减少请求次数，能抓列表页就不抓详情页，减轻服务器压力，程序员都是混口饭吃不容易。
- 不要只看 Web 网站，还有手机 App 和 H5，这样的反爬虫措施一般比较少。
- 实际应用时候，一般防守方做到根据 IP 限制频次就结束了，除非很核心的数据，不会再进行更多的验证，毕竟成本的问题会考虑到。
- 如果真的对性能要求很高，可以考虑多线程(一些成熟的框架如 Scrapy都已支持)，甚至分布式...

### 二、动态HTML介绍

- JavaScript

  JavaScript 是属于网络的脚本语言！

  JavaScript 被数百万计的网页用来改进设计、验证表单、检测浏览器、创建cookies，以及更多的应用。

  JavaScript 是因特网上最流行的脚本语言。

  我们可以在网页源代码的<scripy>标签里看到，比如：

  ```html 
  <script type="text/javascript" src="https://statics.huxiu.com/w/mini/static_2015/js/sea.js?v=201601150944"></script>
  ```

  示例：

  ```html 
  <html>
      <body>
          <script type="text/javascript">
              var r=Math.random()
              if (r>0.5){
                  document.write("学习 Web 开发！")
              }
              else{
                  document.write("访问微软！")
              }
  		</script>
  	</body>
  </html>
  ```

  ​

- jQuery

  jQuery 是一个十分常见的库,70% 最流行的网站(约 200 万)和约 30% 的其他网站(约 2 亿)都在使用。一个网站使用 jQuery 的特征,就是源代码里包含了 jQuery 入口,比如:

  ```html
  <script type="text/javascript" src="https://statics.huxiu.com/w/mini/static_2015/js/jquery-1.11.1.min.js?v=201512181512"></script>
  ```

  代码实例：

  ```html
  <!DOCTYPE html>
  <html>
      <head>
      <meta charset="utf-8">
  		<script 							src="https://cdn.bootcss.com/jquery/1.10.2/jquery.min.js">
          </script>

          <script>
          $(document).ready(function(){
            $("#hide").click(function(){
              $("p").hide();
            });
              	
            $("#show").click(function(){
              $("p").show();
            });
          });
          </script>
  	</head>
  <body>
      <p>如果你点击“隐藏” 按钮，我将会消失。</p>
      <button id="hide">隐藏</button>
      <button id="show">显示</button>
  </body>
  </html>
  ```

  ​

- Ajax


​	我们与网站服务器通信的唯一方式，就是发出 HTTP 请求获取新页面。如果提交表单之后，或从服务器获取信息之后，网站的页面不需要重新刷新，那么你访问的网站就在用Ajax 技术。

Ajax 其实并不是一门语言,而是用来完成网络任务(可以认为 它与网络数据采集差不多)的一系列技术。Ajax 全称是 Asynchronous JavaScript and XML(异步 JavaScript 和 XML)，网站不需要使用单独的页面请求就可以和网络服务器进行交互 (收发信息)。




- DHTML


DHTML 是一种使 HTML 页面具有动态特性的艺术。

DHTML 是一种创建动态和交互 WEB 站点的技术集。

对大多数人来说，DHTML 意味着 HTML、样式表和 JavaScript 的组合



- 直接从 JavaScript 代码里采集内容

  时间成本高可操作性差

  用 Python 的 第三方库运行 JavaScript，直接采集你在浏览器里看到的页面



### 三、Selenium与PhantomJS

**Selenium是一个Web的自动化测试工具**，最初是为网站自动化测试而开发的，类型像我们玩游戏用的按键精灵，可以按指定的命令自动操作，不同是Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器）。

Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。

Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器

Selenium安装：

`pip install selenium`

---



**PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器**，它会把网站加载到内存并执行页面上的 JavaScript，因为不会展示图形界面，所以运行起来比完整的浏览器要高效。

如果我们把 Selenium 和 PhantomJS 结合在一起，就可以运行一个非常强大的网络爬虫了，这个爬虫可以处理 JavaScrip、Cookie、headers，以及任何我们真实用户需要做的事情

[PhantomJS下载安装](http://phantomjs.org/download.html)



- Selenium键盘

  [参考博客](https://www.cnblogs.com/mengyu/p/6942584.html)

  ```python
  from selenium.webdriver.common.keys import Keys
  ```

  | d_keys(Keys.BACK_SPACE)     | 删除键 |
  | --------------------------- | ------ |
  | send_keys(Keys.SPACE)       | 空格键 |
  | send_keys(Keys.TAB)         | 制表键 |
  | send_keys(Keys.ESPACE)      | 回退键 |
  | send_keys(Keys.ENTER)       | 回车键 |
  | send_keys(Keys.CONTROL,'a') | 全选   |
  | send_keys(Keys.CONTROL,'c') | 复制   |
  | send_keys(Keys.CONTROL,'x') | 剪切   |
  | send_keys(Keys.CONTROL,'v') | 粘贴   |
  | send_keys(Keys.F1)          | F1     |

- Selenium使用

  Selenium 库里有个叫 WebDriver 的 API。WebDriver 有点儿像可以加载网站的浏览器，但是它也可以像 BeautifulSoup 或者其他 Selector 对象一样用来查找页面元素，与页面上的元素进行交互 (发送文本、点击等)，以及执行其他动作来运行网络爬虫



### 四、Chrome 内核

- 下载：http://chromedriver.storage.googleapis.com/index.html
- 驱动和浏览器版本对应表：http://blog.csdn.net/huilan_same/article/details/51896672



### 五、Selenium基本操作

- 截屏

  ```python
  from selenium import webdriver
  import time

  path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
  browser = webdriver.PhantomJS(path)

  browser.get('https://movie.douban.com/')

  time.sleep(2)

  browser.save_screenshot('douban2.png')
  ```



- 模拟文本输入搜索前进后退操作

  ```python
  from selenium import webdriver
  import time

  # 创建谷歌浏览器对象, 参数就是谷歌浏览器的驱动
  browser = webdriver.Chrome()

  # 打开网址
  url = 'http://www.baidu.com/'
  browser.get(url)
  time.sleep(2)

  # 找到input框
  # my_input = browser.find_element_by_id('kw')
  # my_input = browser.find_elements_by_xpath('//form[@id="form"]/span[1]/input')[0]
  my_input = browser.find_elements_by_css_selector('#kw')[0]
  my_input.send_keys('美女')
  time.sleep(2)

  # 找到点击按钮点击之 
  my_button = browser.find_element_by_id('su')
  my_button.click()
  time.sleep(2)

  # 模拟浏览器后退操作
  browser.back()
  time.sleep(2)

  browser.forward()
  time.sleep(2)

  browser.quit()
  ```



- 对百度首页进行设置

  ```python
  from selenium import webdriver
  from time import sleep

  driver = webdriver.Chrome()
  # 用get打开百度页面
  driver.get("http://www.baidu.com")
  # 查找页面的“设置”选项，并进行点击
  sleep(2)
  driver.find_elements_by_link_text('设置')[0].click()
  sleep(2)
  # 打开设置后找到“搜索设置”选项，设置为每页显示50条
  driver.find_elements_by_link_text('搜索设置')[0].click()
  sleep(2)
  m = driver.find_element_by_id('nr')
  sleep(2)
  # m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
  m.find_element_by_xpath('.//option[3]').click()
  sleep(2)

  # 点击保存设置
  driver.find_elements_by_class_name("prefpanelgo")[0].click()
  sleep(2)

  # 处理弹出的警告页面   确定accept() 和 取消dismiss()
  # driver.switch_to_alert().accept()
  driver.switch_to.alert.dismiss()
  sleep(2)
  # 找到百度的输入框，并输入 美女
  driver.find_element_by_id('kw').send_keys('美女')
  sleep(2)
  # 点击搜索按钮
  driver.find_element_by_id('su').click()
  sleep(2)
  # 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
  driver.find_elements_by_link_text('美女_百度图片')[0].click()
  sleep(2)

  # 关闭浏览器
  driver.quit()
  ```



- 模拟滚动

  ```python
  from selenium import webdriver
  import time

  driver = webdriver.Firefox()
  url = 'http://sc.chinaz.com/tupian/ribenmeinv.html'
  url = 'https://movie.douban.com/'
  driver.get(url)

  driver.save_screenshot('douban1.png')

  time.sleep(5)

  # chrome浏览器
  js = 'document.body.scrollTop=10000'
  # firefox浏览器
  js = 'document.documentElement.scrollTop=10000'
  driver.execute_script(js)
  driver.save_screenshot('douban2.png')
  time.sleep(5)

  with open('riben.html', 'w', encoding='utf-8') as fp:
  	fp.write(driver.page_source)

  driver.quit()
  ```

  js = 'document.documentElement.scrollTop=10000'
  driver.execute_script(js)



### 六、执行JavaScript语句

```python
js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"
driver.execute_script('$(arguments[0]).fadeOut()',img)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
```

自定义百度页面

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 给搜索输入框标红的javascript脚本
js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"

# 调用给搜索输入框标红js脚本
driver.execute_script(js)

#查看页面快照
driver.save_screenshot("redbaidu.png")

#js隐藏元素，将获取的图片元素隐藏
img = driver.find_element_by_xpath("//div[@id='lg']/img")
driver.execute_script('$(arguments[0]).fadeOut()',img)

time.sleep(5)

driver.get("https://movie.douban.com/")
# 向下滚动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#查看页面快照
driver.save_screenshot("nullbaidu.png")

driver.quit()
```



### 七、模拟网站登录

> 古诗文模拟登录

```python
from selenium import webdriver
import time

url = 'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx/'

driver = webdriver.Chrome()

driver.get(url)

driver.find_element_by_id('email').send_keys('455098435@qq.com')

driver.find_element_by_id('pwd').send_keys('31415926abc')

code = input('请输入验证码：')

driver.find_element_by_id('code').send_keys(code)

driver.find_element_by_id('denglu').click()

time.sleep(20)

driver.quit()
```





