# 爬虫、urllib和Charles

### 1、数据获取方式

- 企业数据：百度指数、阿里指数、微博指数、腾讯指数
- 政府机构数据：[国家数据](http://data.stats.gov.cn/index.htm)、[世界银行](https://data.worldbank.org.cn/)、[纳斯达克](http://www.nasdaq.com/zh) 、[联合国数据](http://data.un.org/)
- 咨询公司：[艾瑞咨询](http://www.iresearch.com.cn/) 、[麦肯锡](https://www.mckinsey.com/)、 [埃森哲](https://www.accenture.com/cn-en)
- 第三方平台：[数据堂](http://www.datatang.com/index.html)、 [国云数据](http://www.moojnn.com/data-market/)、 [贵州大数据交易所](http://trade.gbdex.com/trade.web/)
- 爬虫

### 2、爬虫

- 爬虫：爬取网页数据的程序
- 爬取数据
  - 网页特征：
    - 网页都有唯一的URL（统一资源定位符）来进行定位
    - 都用HTML来描述页面信息
    - 都用HTTP/HTTPS协议来获取页面
  - 爬虫设计思路：
    - 通过URL定位
    - 通过HTTP/HTTPS获取页面
    - 提取HTML需要的数据
- 为什么用Python爬虫？
  - PHP、Java、C/C++、Python都可以爬虫
  - PHP对多线程、异步支持不够好，并发处理弱
  - Java代码量大，重构成本高
  - C/C++学习成本高，代码成型慢
  - Python爬虫代码简洁、效率高、支持模块多
- 使用场景：
  - 通用爬虫：搜索引擎；
  - 聚焦爬虫：面向需求、主题去爬虫

### 3、fiddler

### 4、Charles

### 5、HTTP和https

- 概念
  - Http协议（HyperText Transfer Protocol，超文本传输协议）：是一种发布和接收 HTML页面的方法
  - Https（Hypertext Transfer Protocol over Secure Socket Layer）简单讲是HTTP的安全版，**在HTTP下加入SSL层**
- HTTP通信就是客户端与服务器之间的请求与响应
- **“一次完整的HTTP请求与响应“**参考[这篇博客](https://blog.csdn.net/u010538015/article/details/65631476)。
- cookie和session参考[这篇博客](https://blog.csdn.net/u011816231/article/details/69372208)。

### 6、urllib

- 所谓网页抓取，就是把URL地址中指定的网络资源从网络流中读取出来，保存到本地。 在Python中有很多库可以用来抓取网页，我们先使用urllib

- urlopen

  ```python
  import urllib.request
  # 向指定的url地址发送请求，并返回服务器响应的类文件对象
  response = urllib.request.urlopen("http://www.baidu.com/")

  # 服务器返回的类文件对象支持Python文件对象的操作方法
  # read()方法就是读取文件里的全部内容，返回字符串
  html = response.read().decode('utf-8')
  # 打印响应内容
  print(html)
  ```

- request构造请求对象

  ```python
  import urllib.request

  ua_headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
  }

  # 通过urllib.request.Request() 方法构造一个请求对象
  request = urllib.request.Request("http://www.baidu.com/", headers = ua_headers)

  # 向指定的url地址发送请求，并返回服务器响应的类文件对象
  response = urllib.request.urlopen(request)

  # 服务器返回的类文件对象支持Python文件对象的操作方法
  # read()方法就是读取文件里的全部内容，返回字符串
  html = response.read().decode('utf-8')

  # 返回 HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题
  print(response.getcode())

  # 返回 返回实际数据的实际URL，防止重定向问题
  print(response.geturl())

  # 返回 服务器响应的HTTP报头
  print(response.info())

  # 打印响应内容
  print(html)
  ```

- urllib.request.urlretrieve：加载视频文件等

- urllib.parse.quote/unquote：中文String串编码转换

### 7、User-Agent（用户代理）

- 常用浏览器User-Agent参考[这篇博客](http://blog.csdn.net/u012175089/article/details/61199238)。

  UserAgent中文名为用户代理，是Http协议中的一部分，属于头域的组成部分，这个字符串头主要有下面几部分组成

  1、浏览器标识

  2、操作系统标识

  3、加密等级标识

  4、浏览器语言

  5、渲染引擎

  6、版本信息

  例如Chrome浏览器PC端User-Agent为：`Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36`

- 为什么要用UA用户代理?

  浏览器 就是互联网世界上公认被允许的身份，如果我们希望我们的爬虫程序更像一个真实用户，那我们第一步，就是需要伪装成一个被公认的浏览器。用不同的浏览器在发送请求的时候，会有不同的User-Agent头。会认为是不同的身份。

### 8、get&post

- get请求查询关键字

  ```python
  import urllib
  import urllib.request

  url = "http://www.baidu.com/s"
  headers = {"User-Agent" : "Mozilla......."}
  keyword = input("请输入需要查询的关键字： ")
  wd = {"wd" : keyword}

  # 通过urllib.parse.urlencode() 参数是一个dict类型
  wd = urllib.parse.urlencode(wd)

  # 拼接完整的url
  fullurl = url + "?" + wd

  # 构造请求对象
  request = urllib.request.Request(fullurl, headers = headers)
  response = urllib.request.urlopen(request)
  print(response.read().decode('utf-8'))
  ```

- post

  ```python
  import urllib
  import urllib.request
  import ssl

  content = ssl._create_unverified_context()

  url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%88%B1%E6%83%85"

  headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

  #POST请求和GET请求并没有严格区分，对于GET请求我们也可以通过POST传递参数
  formdata = {
          "start":"0",
          "limit":'2'
      }

  data = urllib.parse.urlencode(formdata).encode('utf-8')

  request = urllib.request.Request(url, data = data, headers = headers)

  response = urllib.request.urlopen(request)
  print(response.geturl())
  print(response.read().decode('utf-8'))
  ```

### 9、SSL证书验证

- 安全认证

  现在随处可见 https 开头的网站，urllib2可以为 HTTPS 请求验证SSL证书，就像web浏览器一样，如果网站的SSL证书是经过CA认证的，则能够正常访问，如：https://www.baidu.com/等...

  如果SSL证书验证不通过，或者操作系统不信任服务器的安全证书，比如浏览器在访问12306网站如：https://www.12306.cn/mormhweb/的时候，会警告用户证书不受信任。

- CA

  CA(Certificate Authority)是数字证书认证中心的简称，是指发放、管理、废除数字证书的受信任的第三方机构，如北京数字认证股份有限公司、上海市数字证书认证中心有限公司等...

  CA的作用是检查证书持有者身份的合法性，并签发证书，以防证书被伪造或篡改，以及对证书和密钥进行管理。

- 安全认证requests

  ```python
  import requests
  url = "https://www.12306.cn/mormhweb/"
  headers = {
      "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
      }
  r = requests.get(url,verify = False)
  print(r.content.decode('utf-8'))
  ```

- 安全认证urllibs

  ```python
  import urllib.request
  import ssl

  ssl._create_default_https_context = ssl._create_unverified_context
  url = "https://www.12306.cn/mormhweb/"

  headers = {
      "User-Agent" : "Mozilla/s5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
      }
  r = urllib.request.urlopen(url=url)
  print(r.read().decode('utf-8'))
  ```

  ​