## 命令
* 创建一个爬虫：scrapy genspider example example.com
* 运行一个爬虫：scrapy crawl chouti  添加--nolog,不打印日志


## settings 介绍
* ROBOTSTXT_OBEY = False 是否遵循爬虫协议
* ITEM_PIPELINES 数据的持久化；数字越小，管道优先级越高
  * 持久化：两种方案
      * scrapy crawl 爬虫名字 -o 文件名.csv  (解析函数返回值必须是列表套字典)
      * pipline持久化：
          * 在Item中写个类（存的字段）
          * 在爬虫的解析中，实例化，并赋值（字典赋值）
          * yield 对象
          * 在pipline中写持久化的类：open_spider，close_spider，process_item（一定要返回，后续才能继续走）
          * 在配置文件中配置pipline（数字越小，优先级越高）
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



## 1 自动给抽屉点赞

```python

from selenium import webdriver
import time
import requests

bro=webdriver.Chrome(executable_path='./chromedriver.exe')
bro.implicitly_wait(10)
bro.get('https://dig.chouti.com/')

login_b=bro.find_element_by_id('login_btn')
print(login_b)
login_b.click()

username=bro.find_element_by_name('phone')
username.send_keys('18953675221')
password=bro.find_element_by_name('password')
password.send_keys('lqz123')

button=bro.find_element_by_css_selector('button.login-btn')
button.click()
# 可能有验证码，手动操作一下
time.sleep(10)


my_cookie=bro.get_cookies()  # 列表
print(my_cookie)
bro.close()

# 这个cookie不是一个字典，不能直接给requests使用，需要转一下
cookie={}
for item in my_cookie:
    cookie[item['name']]=item['value']


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Referer': 'https://dig.chouti.com/'}
# ret = requests.get('https://dig.chouti.com/',headers=headers)
# print(ret.text)


ret=requests.get('https://dig.chouti.com/top/24hr?_=1596677637670',headers=headers)
print(ret.json())
ll=[]
for item in ret.json()['data']:
    ll.append(item['id'])

print(ll)
for id in ll:
    ret=requests.post(' https://dig.chouti.com/link/vote',headers=headers,cookies=cookie,data={'linkId':id})
    print(ret.text)

'https://dig.chouti.com/comments/create'
'''
content: 说的号
linkId: 29829529
parentId: 0

'''
```
