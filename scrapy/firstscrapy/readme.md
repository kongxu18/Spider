## 命令
* 创建一个爬虫：scrapy genspider example example.com
* 运行一个爬虫：scrapy crawl chouti  添加--nolog,不打印日志


## settings 介绍
* ROBOTSTXT_OBEY = False 是否遵循爬虫协议


## 目录介绍
* firstscrapy 项目名字
  * firstscrapy 包
    * spiders 所有爬虫文件
      * baidu.py
    * middlewares.py 中间件
    * pipelines.py 持久化相关（处理items 中类的对象）
    * main 自己加的项目启动文件
    * items.py 一个个类
    * settings 配置文件
  * scrapy.cfg 上线文件