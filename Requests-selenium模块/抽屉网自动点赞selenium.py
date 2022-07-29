from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
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
login_in = driver.find_element(By.XPATH,'//button[contains(@class,"login-btn")]')
login_in.click()

cookies = driver.get_cookies()
cookie = []
for item in cookies:
    cookie.append({item['name']:item['value']})


print(cookie)
# 评论
import time
t = time.gmtime()
driver.close()