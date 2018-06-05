# urllib请求、handler和代理

## 一、get请求：爬取贴吧

```python
#coding=utf-8

import urllib
import urllib.request

def loadPage(url, filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
        filename : 处理的文件名
    """
    print("正在下载 " + filename)
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}

    request = urllib.request.Request(url, headers = headers)
    return urllib.request.urlopen(request).read().decode('utf-8')

def writePage(html, filename):
    """
        作用：将html内容写入到本地
        html：服务器相应文件内容
    """
    print("正在保存 " + filename)
    # 文件写入
    with open(filename, "w",encoding='utf-8') as f:
        f.write(html)
    print("-" * 30)

def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        #print fullurl
        html = loadPage(fullurl, filename)
        print(html)
        #print html
        writePage(html, filename)
        print("谢谢使用")

if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧名:")
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)
```



## 二、post请求

- 百度翻译 `http://fanyi.baidu.com/sug`

  ```python
  import urllib
  import urllib.request
  import urllib.parse
  import json

  # POST
  url = 'http://fanyi.baidu.com/sug'

  key = input('请输入查询的汉字:')

  # fiddler 提供参数:kw=%E5%B0%8F%E6%B2%B3
  params = {'kw':key}

  # TypeError: POST data should be bytes
  params = urllib.parse.urlencode(params).encode('utf-8')

  # ?测试百度翻译是否需要headers
  response = urllib.request.urlopen(url=url,data=params)

  r_text = response.read().decode('utf-8')
  print(type(r_text),r_text)
  with open('./download/cat0.json',mode='w',encoding='utf-8') as file:
      file.write(r_text)

  # 进行json转换
  # loads将字符串转换成json类型数据
  json_obj = json.loads(r_text)
  print(type(json_obj),json_obj)
  with open('./download/cat2.json',mode='w',encoding='utf-8') as file:
      s = '{'
      for key,value in json_obj.items():
          s += '"'+key + '"' +":"+str(value)+','
      s = s[:-1] + '}'
      s = s.replace("'",'"')
      file.write(s)

  # 保存
  # 将json_obj 转化成string
  json_str = json.dumps(json_obj,ensure_ascii=False)
  print(json_str)
  with open('./download/cat.json',mode='w',encoding='utf-8') as file:
      file.write(json_str)

  response = urllib.request.urlopen(url=url,data=params)
  print('---------------',response.read().decode('unicode-escape'))
  ```



- 百度翻译 `http://fanyi.baidu.com/v2transapi`

  ```python
  import urllib
  import urllib.request
  import urllib.parse

  url = 'http://fanyi.baidu.com/v2transapi'

  # 请求头
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
             'Referer': 'http://fanyi.baidu.com/translate',
             'Host': 'fanyi.baidu.com',
             'Cookie':'__cfduid=d4239d00cf28765faa236f6608b6608881505905792; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1516063589; BAIDUID=08FF61A25E088F1E52D00EFF1BF6553D:SL=0:NR=50:FG=1; BDUSS=nJXWmdoSVl6S1JIWXdWNjQ0MTJ5OFVpOC1ZZElWZzFqLTg1UXhIazAyY2ctUFJhQVFBQUFBJCQAAAAAAAAAAAEAAADcsb9ywre34cCkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBrzVoga81aV; BIDUPSID=3F36E6E1D84B20491F59AC388BCE71F2; cflag=15%3A3; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; PSINO=2; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1433_21119_26350_20928; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1527219467; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1527219467; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D'}

  # 请求体
  data = {'from':'zh',
          'to':'en',
          'query':'图片',
          'transtype':'realtime',
          'simple_means_flag':3,
          'sign':'76488.379385',
          'token':'6c98653b52133a314c97d378260dd23f'}

  params = urllib.parse.urlencode(data).encode('utf-8')

  request = urllib.request.Request(url=url,data=params,headers=headers)

  # 发起请求
  response = urllib.request.urlopen(request)

  print(response.read().decode('unicode-escape'))

  # 总结:爬虫时候,请求的参数至关重要的,一个都不能少,正确获取关键
  ```



## 三、ajax请求



- get ：[豆瓣动作电影排行]( https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20)

  ​


- Post：[肯德基](http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname)

  ```python
  import urllib.request
  import urllib.parse

  data = {
  	'cname': '北京',
  	'pid': '',
  	'pageIndex': '3',
  	'pageSize': '10',
  }
  data = urllib.parse.urlencode(data).encode('utf-8')

  url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

  headers = {
  	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
  }

  request = urllib.request.Request(url=url, headers=headers, data=data)
  reponse = urllib.request.urlopen(request)

  print(reponse.read().decode('utf-8'))
  ```



## 四、URLError和HTTPError

- URLError

  - 没有网络连接

  - 服务器连接失败

  - 找不到指定服务器

  - try except捕获异常

    ```python
    import urllib2

    request = urllib2.Request('http://www.fsujsjfsalsjfks.com')

    try:
        urllib2.urlopen(request, timeout=5)
        print('okay')
    except Exception as err:
        print('hello')
        print(err)
    ```

- HTTPError

  HTTPError是URLError的子类，我们发出一个请求时，服务器上都会对应一个response应答对象，其中它包含一个数字"响应状态码"


  如果urlopen或opener.open不能处理的，会产生一个HTTPError，对应相应的状态码，HTTP状态码表示HTTP协议所返回的响应的状态。

  注意，urllib可以为我们处理重定向的页面（也就是3开头的响应码），100-299范围的号码表示成功，所以我们只能看到400-599的错误号码

### 常见响应错误码



1xx:信息  

| 100 Continue            | 服务器仅接收到部分请求，但是一旦服务器并没有拒绝该请求，客户端应该继续发送其余的请求。 |
| ----------------------- | ------------------------------------------------------------ |
| 101 Switching Protocols | 服务器转换协议：服务器将遵从客户的请求转换到另外一种协议。   |

2xx:成功

| 200 OK                            | 请求成功（其后是对GET和POST请求的应答文档）                  |
| --------------------------------- | ------------------------------------------------------------ |
| 201 Created                       | 请求被创建完成，同时新的资源被创建。                         |
| 202 Accepted                      | 供处理的请求已被接受，但是处理未完成。                       |
| 203 Non-authoritative Information | 文档已经正常地返回，但一些应答头可能不正确，因为使用的是文档的拷贝。 |
| 204 No Content                    | 没有新文档。浏览器应该继续显示原来的文档。如果用户定期地刷新页面，而Servlet可以确定用户文档足够新，这个状态代码是很有用的。 |
| 205 Reset Content                 | 没有新文档。但浏览器应该重置它所显示的内容。用来强制浏览器清除表单输入内容。 |
| 206 Partial Content               | 客户发送了一个带有Range头的GET请求，服务器完成了它。         |

3xx:重定向  

| 300 Multiple Choices   | 多重选择。链接列表。用户可以选择某链接到达目的地。最多允许五个地址。 |
| ---------------------- | ------------------------------------------------------------ |
| 301 Moved Permanently  | 所请求的页面已经转移至新的url。                              |
| 302 Moved Temporarily  | 所请求的页面已经临时转移至新的url。                          |
| 303 See Other          | 所请求的页面可在别的url下被找到。                            |
| 304 Not Modified       | 未按预期修改文档。客户端有缓冲的文档并发出了一个条件性的请求（一般是提供If-Modified-Since头表示客户只想比指定日期更新的文档）。服务器告诉客户，原来缓冲的文档还可以继续使用。 |
| 305 Use Proxy          | 客户请求的文档应该通过Location头所指明的代理服务器提取。     |
| 306 Unused             | 此代码被用于前一版本。目前已不再使用，但是代码依然被保留。   |
| 307 Temporary Redirect | 被请求的页面已经临时移至新的url。                            |



4xx:客户端错误  

| 400 Bad Request                     | 服务器未能理解请求。                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| 401 Unauthorized                    | 被请求的页面需要用户名和密码。                               |
| 401.1                               | 登录失败。                                                   |
| 401.2                               | 服务器配置导致登录失败。                                     |
| 401.3                               | 由于 ACL 对资源的限制而未获得授权。                          |
| 401.4                               | 筛选器授权失败。                                             |
| 401.5                               | ISAPI/CGI 应用程序授权失败。                                 |
| 401.7                               | 访问被 Web 服务器上的 URL 授权策略拒绝。这个错误代码为 IIS 6.0 所专用。 |
| 402 Payment Required                | 此代码尚无法使用。                                           |
| 403 Forbidden                       | 对被请求页面的访问被禁止。                                   |
| 403.1                               | 执行访问被禁止。                                             |
| 403.2                               | 读访问被禁止。                                               |
| 403.3                               | 写访问被禁止。                                               |
| 403.4                               | 要求 SSL。                                                   |
| 403.5                               | 要求 SSL 128。                                               |
| 403.6                               | IP 地址被拒绝。                                              |
| 403.7                               | 要求客户端证书。                                             |
| 403.8                               | 站点访问被拒绝。                                             |
| 403.9                               | 用户数过多。                                                 |
| 403.10                              | 配置无效。                                                   |
| 403.11                              | 密码更改。                                                   |
| 403.12                              | 拒绝访问映射表。                                             |
| 403.13                              | 客户端证书被吊销。                                           |
| 403.14                              | 拒绝目录列表。                                               |
| 403.15                              | 超出客户端访问许可。                                         |
| 403.16                              | 客户端证书不受信任或无效。                                   |
| 403.17                              | 客户端证书已过期或尚未生效。                                 |
| 403.18                              | 在当前的应用程序池中不能执行所请求的 URL。这个错误代码为 IIS 6.0 所专用。 |
| 403.19                              | 不能为这个应用程序池中的客户端执行 CGI。这个错误代码为 IIS 6.0 所专用。 |
| 403.20                              | Passport 登录失败。这个错误代码为 IIS 6.0 所专用。           |
| 404 Not Found                       | 服务器无法找到被请求的页面。                                 |
| 404.0                               | 没有找到文件或目录。                                         |
| 404.1                               | 无法在所请求的端口上访问 Web 站点。                          |
| 404.2                               | Web 服务扩展锁定策略阻止本请求。                             |
| 404.3                               | MIME 映射策略阻止本请求。                                    |
| 405 Method Not Allowed              | 请求中指定的方法不被允许。                                   |
| 406 Not Acceptable                  | 服务器生成的响应无法被客户端所接受。                         |
| 407 Proxy Authentication Required   | 用户必须首先使用代理服务器进行验证，这样请求才会被处理。     |
| 408 Request Timeout                 | 请求超出了服务器的等待时间。                                 |
| 409 Conflict                        | 由于冲突，请求无法被完成。                                   |
| 410 Gone                            | 被请求的页面不可用。                                         |
| 411 Length Required                 | "Content-Length" 未被定义。如果无此内容，服务器不会接受请求。 |
| 412 Precondition Failed             | 请求中的前提条件被服务器评估为失败。                         |
| 413 Request Entity Too Large        | 由于所请求的实体的太大，服务器不会接受请求。                 |
| 414 Request-url Too Long            | 由于url太长，服务器不会接受请求。当post请求被转换为带有很长的查询信息的get请求时，就会发生这种情况。 |
| 415 Unsupported Media Type          | 由于媒介类型不被支持，服务器不会接受请求。                   |
| 416 Requested Range Not Satisfiable | 服务器不能满足客户在请求中指定的Range头。                    |
| 417 Expectation Failed              | 执行失败。                                                   |
| 423                                 | 锁定的错误。                                                 |

  

5xx:服务器错误  

| 500 Internal Server Error      | 请求未完成。服务器遇到不可预知的情况。                |
| ------------------------------ | ----------------------------------------------------- |
| 500.12                         | 应用程序正忙于在 Web 服务器上重新启动。               |
| 500.13                         | Web 服务器太忙。                                      |
| 500.15                         | 不允许直接请求 Global.asa。                           |
| 500.16                         | UNC 授权凭据不正确。这个错误代码为 IIS 6.0 所专用。   |
| 500.18                         | URL 授权存储不能打开。这个错误代码为 IIS 6.0 所专用。 |
| 500.100                        | 内部 ASP 错误。                                       |
| 501 Not Implemented            | 请求未完成。服务器不支持所请求的功能。                |
| 502 Bad Gateway                | 请求未完成。服务器从上游服务器收到一个无效的响应。    |
| 502.1                          | CGI 应用程序超时。                                    |
| 502.2                          | CGI 应用程序出错。                                    |
| 503 Service Unavailable        | 请求未完成。服务器临时过载或当机。                    |
| 504 Gateway Timeout            | 网关超时。                                            |
| 505 HTTP Version Not Supported | 服务器不支持请求中指明的HTTP协议版本。                |

 

## 五、cookie模拟登录

### 1、cookie

Cookie 是指某些网站服务器为了辨别用户身份，而储存在用户浏览器上的文本文件，Cookie可以保持登录信息到用户下次与服务器的会话

HTTP是无状态的面向连接的协议, 为了保持连接状态, 引入了Cookie机制 Cookie是http消息头中的一种属性



### 2、cookie结构

Cookie名字（Name）
Cookie的值（Value）
Cookie的过期时间（Expires/Max-Age）
Cookie作用路径（Path）
Cookie所在域名（Domain），
使用Cookie进行安全连接（Secure）


前两个参数是Cookie应用的必要条件

Cookie格式：
Set－Cookie: NAME=VALUE；Expires=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE



### 3、cookie应用

Cookies在爬虫方面最典型的应用是判定注册用户是否已经登录网站，用户可能会得到提示，是否在下一次进入此网站时保留用户信息以便简化登录手续





### 4、登录人人网

```python
import urllib
import urllib.request
# 1. 构建一个已经登录过的用户的headers信息
headers = {
    "Host":"www.renren.com",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    # 便于终端阅读，表示不支持压缩文件
    # Accept-Encoding: gzip, deflate, sdch,
    # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
    "Cookie": "…………"
}
# 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象
request = urllib.request.Request(url = 'http://www.renren.com/960222034',headers=headers)

response = urllib.request.urlopen(request)

# 3. 打印响应内容
print(response.read().decode('utf-8'))
```

### 5、登录微博

```python
import urllib.request

url = 'https://weibo.com/u/6433251843/home'
headers = {
	'Host': 'weibo.com',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Referer': 'https://weibo.com/',
	# 'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cookie':'……'
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

with open('weibo3.html', 'w',encoding='utf-8') as fp:
	fp.write(response.read().decode('utf-8'))
```



## 六、handler

- Handler：HTTP处理器对象，支持处理HTTP请求

  - 前面学习的urllib.request.urlopen()很简单的一个获取网页的函数，但是它不能自己构建请求头
  - 引入了request对象，request = urllib.request.Request(url=url, headers=headers),它的高级之处就是可以自己定制请求头
  - request对象不能使用代理，所以引入了Handler处理器、自定义Opener

- 使用Handler创建urlOpener

  ```python
  import urllib.request

  # 首先创建一个handler对象
  handler = urllib.request.HTTPHandler()

  # 创建opener对象
  opener = urllib.request.build_opener(handler)

  # 构建请求对象
  url = 'http://www.baidu.com/'
  headers = {
  	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
  }
  request = urllib.request.Request(url=url, headers=headers)

  response = opener.open(request)

  print(response.read().decode('utf-8'))
  ```



## 七、开发代理和私密代理的使用



### 1、开放代理

- 代理IP

  使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。

  很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。

  所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。

  urllib中通过ProxyHandler来设置使用代理服务器，下面代码说明如何使用自定义opener来使用代理：

- 代理

  免费的开放代理获取基本没有成本，我们可以在一些代理网站上收集这些免费代理，测试后如果可以用，就把它收集起来用在爬虫上面。

- Proxyhandler

  ```python
  import urllib
  import urllib.request

  # 代理开关，表示是否启用代理
  proxyswitch = True
  httpproxy_handler = urllib.request.ProxyHandler({"https" : '117.90.3.243:9000'})

  # 构建了一个没有代理的处理器对象
  nullproxy_handler = urllib.request.ProxyHandler({})

  if proxyswitch:
      opener = urllib.request.build_opener(httpproxy_handler)
  else:
      opener = urllib.request.build_opener(nullproxy_handler)

  # 使用opener打开联网请求
  response = opener.open('http://www.baidu.com/')
  print(response.read().decode('utf-8'))


  # 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送
  # urllib.request.install_opener(opener)
  # request = urllib.request.Request("http://www.baidu.com/")
  # response = urllib.request.urlopen(request)
  # print(response.read().decode('utf-8'))
  ```

- ProxyBasicAuthHandler(代理授权认证)

  ```python
  import urllib
  import urllib.request
  import os
  # 私密代理授权的账户
  user = os.environ.get('proxyuser')
  # 私密代理授权的密码
  passwd = os.environ.get('proxypassword')
  # 私密代理 IP
  proxyserver = os.environ.get('proxyserver')
  print(user,passwd,proxyserver)

  # 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
  passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

  # 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般都是写None，后面三个参数分别是 代理服务器、用户名、密码
  passwdmgr.add_password(None, proxyserver, user, passwd)

  # 3. 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
  #   注意，这里不再使用普通ProxyHandler类了
  proxyauth_handler = urllib.request.ProxyBasicAuthHandler(passwdmgr)

  # 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象
  opener = urllib.request.build_opener(proxyauth_handler)

  # 5. 构造Request 请求
  request = urllib.request.Request("http://www.baidu.com/")

  # 6. 使用自定义opener发送请求
  response = opener.open(request)

  # 7. 打印响应内容
  print(response.read().decode('utf-8'))
  ```



## 八、CookieJar

cookiejar模块：主要作用是提供用于存储cookie的对象

该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。

CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向下一次发出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

其实大多数情况下，我们只用CookieJar()

在Python处理Cookie，一般是通过cookielib模块和 urllib模块的HTTPCookieProcessor处理器类一起使用.

- HTTPCookieProcessor处理器：主要作用是处理这些cookie对象，并构建handler对象

> 模拟登录

- 登录[豆瓣](https://www.douban.com/accounts/login)url抓取

- 登录

  ```python
  import http.cookiejar as cookiejar
  import urllib
  import urllib.request

  # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
  cookie = cookiejar.CookieJar()

  # 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
  cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

  # 构建一个自定义的opener
  opener = urllib.request.build_opener(cookie_handler)

  # 通过自定义opener的addheaders的参数，可以添加HTTP报头参数
  opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

  # renren网的登录接口
  url = "https://www.douban.com/accounts/login"

  # 需要登录的账户密码
  data = {"form_email":"18513106743",
          "form_password":"31415926abc",
          }

  # 通过urlencode()编码转换
  data = urllib.parse.urlencode(data).encode(encoding='UTF8')

  # 设置全局urllib
  urllib.request.install_opener(opener)

  # 第一次是post请求，发送登录需要的参数，获取cookie
  request = urllib.request.Request(url, data = data)

  # 发送第一次的post请求，生成登录后的cookie(如果登录成功的话)
  response = opener.open(request)

  # print(response.read().decode(encoding = 'UTF-8'))

  #第二次登录无需cookie
  url = r'https://www.douban.com/people/164698173/'
  response = urllib.request.urlopen(url)

  print(response.read().decode('utf-8'))
  ```

- 模拟登录需要注意的点

  - 登录一般都会先有一个HTTP GET，用于拉取一些信息及获得Cookie，然后再HTTP POST登录。

  - HTTP POST登录的链接有可能是动态的，从GET返回的信息中获取。

  - password 有些是明文发送，有些是加密后发送。有些网站甚至采用动态加密的，同时包括了很多其他数据的加密信息，只能通过查看JS源码获得加密算法，再去破解加密，非常困难

  - 大多数网站的登录整体流程是类似的，可能有些细节不一样，所以不能保证其他网站登录成功

  - 模拟登陆问题 ：当然，我们也可以直接发送账号密码到登录界面模拟登录，但是当网页采用JavaScript动态技术以后，想封锁基于 HttpClient 的模拟登录就太容易了，甚至可以根据你的鼠标活动的特征准确地判断出是不是真人在操作。

    所以，想做通用的模拟登录还得选别的技术，比如用内置浏览器引擎的爬虫(关键词：Selenium ，PhantomJS)，这个我们将在以后会学习到



## 九、web客户端授权认证

**HTTPBasicAuthHandler(Web客户端授权验证)**

```python
import urllib
import urllib.request

user = "admin"
password = "123456"
webserver = "192.168.28.1"

# 构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
passwordMgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加授权账户信息，第一个参数realm如果没有指定就写None，后三个分别是站点IP，账户和密码
passwordMgr.add_password(None, webserver, user, password)

# HTTPBasicAuthHandler() HTTP基础验证处理器类
proxyauth_handler = urllib.request.HTTPBasicAuthHandler(passwordMgr)

# 构建自定义opener
opener = urllib.request.build_opener(proxyauth_handler)

request = urllib.request.Request("http://192.168.28.1/")

# 用授权验证信息
response = opener.open(request)

print(response.read().decode('utf-8'))

```

