


from selenium import webdriver
import time
#pillow
from PIL import Image

# 引入超级鹰

from chaojiying import Chaojiying_Client


from selenium.webdriver import ActionChains
bro=webdriver.Chrome(executable_path='./chromedriver.exe')
bro.implicitly_wait(10)
try:
    bro.get('https://kyfw.12306.cn/otn/resources/login.html')
    bro.maximize_window()  # 窗口最大化，全屏
    button_z=bro.find_element_by_css_selector('.login-hd-account a')
    button_z.click()
    time.sleep(2)
    # 截取整个屏幕
    bro.save_screenshot('./main.png')
    # 验证码的位置和大小
    img_t=bro.find_element_by_id('J-loginImg')
    print(img_t.size)
    print(img_t.location)

    size=img_t.size
    location=img_t.location

    img_tu = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
    # # 抠出验证码
    # #打开
    img = Image.open('./main.png')
    # 抠图
    fram = img.crop(img_tu)
    # 截出来的小图
    fram.save('code.png')

    # 调用超级鹰破解
    chaojiying = Chaojiying_Client('306334678', 'lqz12345', '903641')	#用户中心>>软件ID 生成一个替换 96001
    im = open('code.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # print(chaojiying.PostPic(im, 9004))

    ## 返回结果如果有多个 260,133|123，233,处理这种格式[[260,133],[123,233]]
    res=chaojiying.PostPic(im, 9004)
    print(res)
    result=res['pic_str']

    all_list = []
    if '|' in result:
        list_1 = result.split('|')
        count_1 = len(list_1)
        for i in range(count_1):
            xy_list = []
            x = int(list_1[i].split(',')[0])
            y = int(list_1[i].split(',')[1])
            xy_list.append(x)
            xy_list.append(y)
            all_list.append(xy_list)
    else:
        x = int(result.split(',')[0])
        y = int(result.split(',')[1])
        xy_list = []
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
    print(all_list)
    # 用动作链，点击图片
    # [[260,133],[123,233]]
    for a in all_list:
        x = a[0]
        y = a[1]
        ActionChains(bro).move_to_element_with_offset(img_t, x, y).click().perform()
        time.sleep(1)

    username=bro.find_element_by_id('J-userName')
    username.send_keys('306334678')
    password=bro.find_element_by_id('J-password')
    password.send_keys('lqz12345')
    time.sleep(3)
    submit_login=bro.find_element_by_id('J-login')
    submit_login.click()
    time.sleep(3)

    print(bro.get_cookies())
    time.sleep(10)
    bro.get('https://www.12306.cn/index/')
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    bro.close()