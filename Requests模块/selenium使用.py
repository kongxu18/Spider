"""
selenium
解决requests 无法直接执行javascript代码的问题

驱动地址：https://npmmirror.com/

"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

"""
无头浏览器
"""
chrome_options = Options()
# 指定分辨率
chrome_options.add_argument('window-size=1920*1080')
# 谷歌文档：加上这个属性规避bug
chrome_options.add_argument('--disable-gpu')
# 隐藏滚动条
chrome_options.add_argument('--hide-scrollbars')
# 不加载图片，提高速度
chrome_options.add_argument('blink-settings=imagesEnabled=false')
# 浏览器不提供可视化页面，linux 下如果系统不支持可视化不加这个会启动失败,这条就实现了无头浏览器
chrome_options.add_argument('--headless')
# 手动指定浏览器位置
# chrome_options.binary_location=r'C:\Program Files\...'


# 指定使用的驱动，也可以放在python的scripts目录下
ser = Service(executable_path='chromedriver.exe')
bro = webdriver.Chrome(service=ser, options=chrome_options)

bro.get('https://www.baidu.com')
time.sleep(2)
print(bro.page_source)
bro.close()

# 获取元素属性
tag = bro.find_element(by=By.ID, value='a')

# 找当前控件的 属性
tag.get_attribute('href')

a = tag.text  # 文本
a = tag.location  # 位置
a = tag.tag_name  # 标签名称
a = tag.size  # 标签大小

# 元素交互
tag.send_keys()  # 输入
tag.click()  # 点击
tag.clear()  # 清空

"""
执行js
作用:控制台执行js代码
"""
bro.execute_script('alert(111)')

"""
html 里面套一个html：frame
<frame/> 标签切换
"""
bro.switch_to.frame('frame_name')

"""
选项卡切换
"""
window_handles = bro.window_handles  # 获取所有选项卡
bro.switch_to.window(window_handles[0])  # 操作第一个选项卡


"""
模拟浏览器前进后退
"""
bro.back()
bro.forward()

"""
cookies
"""
cookie = bro.get_cookies()
bro.add_cookie(cookie)
bro.delete_all_cookies()


"""
动作链
"""