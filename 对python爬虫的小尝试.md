# 对python爬虫的小尝试 
概要：利用强大的python+PlantformJS+Selenium实现对各种网页元素的数据筛检和处理。

## 预备知识
1. python(至少学到在python中**面向对象编程的知识**)
2. html常识,包括:
标签(常见标签如 <a> <b> <br /> <div> <p> <html> <body> <head> <)
元素(标签➕标签内容)
属性(常见属性有 style, hrel, alt,  name, src>
样式(知道怎么设置样式,在html文档设置样式的三种方式)
3. 如何配置js环境(**phantomjs要用!!!**)
## 工具：
1. *requests库*：用于给网站发送各种Http请求来获取网站的数据
2. *BeautifulSoup库*：从html 文本中提取数据
3. *os库*：添加创建目录的方法
4. *phantform*:
PhatomJS是一个WebKit内核的浏览器引擎，
它能像浏览器一样（它就是一个浏览器，只不过没有界面）解析网页，以及运行JavaScript脚本。[^引文]
5. *Selenium*(**注意需要2.44版!,新版已不再提供对phantomos的支持**):
Selenium是一个自动化测试框架,用于模拟人工操作以实现自动化。
“Selenium是一个自动化测试框架，广泛的用于自动化测试领域（是不是真的广泛用于自动化测试领域我也不知道，没怎么搞过自动化测试 -_-!，这是我臆测的 =￣ω￣=）。因为它能够模拟人工操作，比如能在浏览器中点击按钮、在输入框中输入文本、自动填充表单、还能进行浏览器窗口的切换、对弹出窗口进行操作。也就是说你能手动做的东西，基本都能用它来实现自动化！”[^引文]
6. python3(这个都知道的)
7. node.js(js环境)
## 学习过程
1. 学习python(周一<--------->周六中午)
每天平均抽出两个多小时学习了python从*列表*到*类*的知识
初步的懂得了python的编程格式和方法。
2. 强入实战（周六中午<----------->周日晚）
### 时间线
<周六下午>
浏览面向小白的爬虫编写教程，
发现需要html知识
学习html基本知识（大约花了5个小时）
休息
</周六晚>
<周日白天>
    继续肝python爬虫小白教程
    发现基本看不懂（基本全篇在用面向对象编程）
    按照我对面向对象编程粗浅的理解去揣测大佬的代码的意思(来回比对各种教程，肝了4～5个小时）
    大概了解了，开始肝代码（肝了40分钟左右）
    发现出现各种问题：
        1. 找不到在pipenv上安装的库。
                解决办法：只能调用pieniv自己的虚拟环境python来使用     库。
        2.一段非常长的错误信息，大概和这个错误信息相似
        ```
        Traceback (most recent call last):
        File "E:/~PROJECT/disinfo/py/bs.py", line 8, in <module>
        driver = webdriver.PhantomJS('C:/Program Files (x86)/phantomjs-1.9.2-windows')
        File "C:\Python27\lib\site-packages\selenium\webdriver\phantomjs\webdriver.py", line 50, in __init__
        self.service.start()
        File "C:\Python27\lib\site-packages\selenium\webdriver\phantomjs\service.py", line 63, in start
        raise WebDriverException("Unable to start phantomjs with ghostdriver.", e)
        selenium.common.exceptions.WebDriverException: Message: 'Unable to start phantomjs with ghostdriver.' ; Screenshot: available via screen 
        ```
        大概说是找不到phantomjs？？我才刚刚安装好不。。。
        解决办法：在查阅数小时网上资料后得到。在调用PhantomJS( ) 时添加参数`executable_path=`
        3. 检查文件重名时提示找不到目录
        解决方法：暂时未找到
        4. 加载了request库却无法使用request方法（在教程上就这样写啊？）
            解决方法：用requests.get()代替self.request()
        5. 各种拼写问题
    然后就到半夜11点多了，继续肝markdown文档（心里苦）
</周日晚>


