# Windows下更换Python清华源

- 打开文件管理器，地址栏输入`%appdata%`

![%appdata%](.\Markdown图片\%appdata%.png)



- 进入到`C:\Users\wu\AppData\Roaming`文件夹，创建`pip`文件夹，并在里面创建`pip.ini`文件

![folder_pip](.\Markdown图片\folder_pip.png)

- 配置文件输入下面内容，保存

  ```ini
  [global]
  timeout = 6000
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  trusted-host = pypi.tuna.tsinghua.edu.cn
  ```

  ​

  ![pip.ini](.\Markdown图片\pip.ini.png)



![pip.ini](.\Markdown图片\pip.ini文件.png)



# 以后使用的pip就是用的清华源了

