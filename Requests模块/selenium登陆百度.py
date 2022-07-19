"""
bro 显示等待/隐式等待

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 指定使用的驱动，也可以放在python的scripts目录下
ser = Service(executable_path='chromedriver.exe')
bro = webdriver.Chrome(service=ser)

# 隐式等待
# 所有查询控件，如果没有找到，就等待5秒，没找到再报错
bro.implicitly_wait(60)

bro.get('https://www.baidu.com')

# bro.find_element(by=By.ID, value='kw')

input = bro.find_element(by=By.XPATH, value='//input[@id="kw"]')
input.send_keys('美女')

search = bro.find_element(by=By.XPATH, value='//input[@type="submit" and @id="su"]')
search.click()

# 登陆百度
# a 标签内容找
time.sleep(1)
button = bro.find_element(by=By.XPATH, value='//a[@name="tj_login"]')
button.click()


login = bro.find_element(by=By.ID,value='TANGRAM__PSP_11__changePwdCodeItem')
login.click()


username = bro.find_element(By.ID,'TANGRAM__PSP_11__userName')
username.send_keys('紫华99')

password = bro.find_element(By.ID,'TANGRAM__PSP_11__password')
password.send_keys('33333a521/')

login = bro.find_element(By.XPATH,'//input[@id="TANGRAM__PSP_11__submit"]')
login.click()

time.sleep(15)
cookie = bro.get_cookies()
print(cookie)