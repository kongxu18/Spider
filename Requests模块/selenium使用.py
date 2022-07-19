"""
selenium
解决requests 无法直接执行javascript代码的问题

"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 指定使用的驱动，也可以放在python的scripts目录下
ser = Service(executable_path='chromedriver.exe')
bro  = webdriver.Chrome(service=ser)


bro.get('https://www.baidu.com')
time.sleep(2)
print(bro.page_source)
bro.close()