# 今日内容

## 1 scrapy 介绍，架构介绍（框架）

```python
#1  通用的网络爬虫框架,爬虫界的django
#2 scrapy执行流程
	5大组件
    	-引擎(EGINE)：大总管，负责控制数据的流向
        -调度器(SCHEDULER)：由它来决定下一个要抓取的网址是什么，去重
        -下载器(DOWLOADER)：用于下载网页内容, 并将网页内
        容返回给EGINE，下载器是建立在twisted这个高效的异步模型上的
        -爬虫(SPIDERS):开发人员自定义的类，用来解析responses，并且提取items，或者发送新的请求request
        -项目管道(ITEM PIPLINES):在items被提取后负责处理它们，主要包括清理、验证、持久化（比如存到数据库）等操作
	2大中间件
    	-爬虫中间件：位于EGINE和SPIDERS之间，主要工作是处理SPIDERS的输入和输出（用的很少）
        -下载中间件：引擎和下载器之间，加代理，加头，集成selenium        
        
# 3 开发者只需要在固定的位置写固定的代码即可（写的最多的spider）
```



## 2 scrapy安装（windows，mac，linux）

```python
#1 pip3 install scrapy（mac，linux）
#2 windows上（80%能成功，少部分人成功不了）
	1、pip3 install wheel #安装后，便支持通过wheel文件安装软件，wheel文件官网：https://www.lfd.uci.edu/~gohlke/pythonlibs
    3、pip3 install lxml
    4、pip3 install pyopenssl
    5、下载并安装pywin32：https://sourceforge.net/projects/pywin32/files/pywin32/
    6、下载twisted的wheel文件：http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    7、执行pip3 install 下载目录\Twisted-17.9.0-cp36-cp36m-win_amd64.whl
    8、pip3 install scrapy
# 3 就有scrapy命令
	-D:\Python36\Scripts\scrapy.exe  用于创建项目
```



## 3 scrapy 创建项目，创建爬虫，运行爬虫

```python
1 scrapy startproject 项目名
	-scrapy startproject firstscrapy
2 创建爬虫
	-scrapy genspider 爬虫名 爬虫地址
    -scrapy genspider chouti dig.chouti.com
    -一执行就会在spider文件夹下创建出一个py文件，名字叫chouti
3 运行爬虫
	-scrapy crawl chouti   # 带运行日志
    -scrapy crawl chouti --nolog  # 不带日志
4 支持右键执行爬虫
	-在项目路径下新建一个main.py
    from scrapy.cmdline import execute
	execute(['scrapy','crawl','chouti','--nolog'])
```



## 4 目录介绍

```python

    # 目录介绍
    firstscrapy  # 项目名字
        firstscrapy # 包
            -spiders # 所有的爬虫文件放在里面
                -baidu.py # 一个个的爬虫（以后基本上都在这写东西）
                -chouti.py
            -middlewares.py # 中间件（爬虫，下载中间件都写在这）
            -pipelines.py   # 持久化相关写在这（items.py中类的对象）
            -main.py        # 自己加的，执行爬虫
            -items.py       # 一个一个的类，
            -settings.py    # 配置文件
        scrapy.cfg          # 上线相关
```



## 5 settings介绍

```python
1 默认情况，scrapy会去遵循爬虫协议
2 修改配置文件参数，强行爬取，不遵循协议
	-ROBOTSTXT_OBEY = False
3 USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
4 LOG_LEVEL='ERROR'
```



## 6 爬取抽屉新闻

```python
# 详见代码
```



## 7 scrapy的数据解析（重点）

```python

#xpath：
    -response.xpath('//a[contains(@class,"link-title")]/text()').extract()  # 取文本
    -response.xpath('//a[contains(@class,"link-title")]/@href').extract()  #取属性
#css
    -response.css('.link-title::text').extract()  # 取文本
    -response.css('.link-title::attr(href)').extract_first()  # 取属性

```



## 8 scrapy的持久化存储（重点）

```python
#1 方案一：parser函数必须返回列表套字典的形式（了解）
	scrapy crawl chouti -o chouti.csv
#2 方案二：高级，pipline item存储（mysql，redis，文件）
	-在Items.py中写一个类
    -在spinder中导入，实例化，把数据放进去
    	    item['title']=title
            item['url']=url
            item['photo_url']=photo_url
            yield item
            
    -在setting中配置（数字越小，级别越高）
    	ITEM_PIPELINES = {
   		'firstscrapy.pipelines.ChoutiFilePipeline': 300,
		}
    -在pipelines.py中写ChoutiFilePipeline
    	-open_spider（开始的时候）
        -close_spider（结束的时候）
        -process_item（在这持久化）
```

# 补充

```python
https://www.cnblogs.com/PythonLearner/p/13424051.html
    
https://juejin.im/post/6857287743966281736
```

# 作业：

```python
1 新建scrapy项目，爬取抽屉数据，存到redis和mysql中
2 读http协议文章并整理https://juejin.im/post/6857287743966281736
3 爬取cnblogs首页文章，打印出标题和连接地址
4 （部分）爬取cnblogs文章，把标题连接地址和文章内容保存到mysql，连续爬取n页
5 （部分）登录到抽屉获取cookie，使用requests给文章点赞
```