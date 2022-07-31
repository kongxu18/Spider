import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time, datetime
from lxml import etree

# ser = Service(executable_path='')
driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('https://dig.chouti.com/')

login_btn = driver.find_element(by=By.XPATH, value='//a[@id="login_btn"]')
login_btn.click()

phone = driver.find_element(By.XPATH, '//input[@name="phone"]')
phone.send_keys('15000876583')

password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys('333333/')

"""
在这里有一个坑，命令输入太快，居然会把按钮设置为禁止点击
"""
time.sleep(1)
login_in = driver.find_element(By.XPATH, '//button[contains(@class,"login-btn")]')
time.sleep(5)
login_in.click()
time.sleep(10)
"""
selenium 可能获取的cookie 不全，使用js
"""
driver.refresh()
time.sleep(1)

cookies = driver.get_cookies()

# get_cookie_js = 'return document.cookie'
# cookie = driver.execute_script(get_cookie_js)
#
# with open('cookie.txt','w',encoding='utf8') as f:
#     f.write(cookie)


cookie = {}
for item in cookies:
    cookie[item['name']] = item['value']

header_dict = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "15",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Cookie": f"{cookie}",
    "Host": "dig.chouti.com",
    "Origin": "https://dig.chouti.com",
    "Referer": "https://dig.chouti.com/",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "X-Requested-With": "XMLHttpRequest"
}
argument = requests.post('https://dig.chouti.com/link/vote', headers=header_dict,cookies=cookie,
                         data={'linkId': "35838202"})
print(argument.text)

driver.close()
