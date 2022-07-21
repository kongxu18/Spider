from selenium import webdriver
import time
# 模拟键盘输入
from selenium.webdriver.common.keys import Keys
bro=webdriver.Chrome(executable_path='./chromedriver.exe')
# 设置隐士等待
bro.implicitly_wait(10)


def get_goods_info(bro):
    # li_list=bro.find_element_by_class_name('gl-warp').find_elements_by_tag_name('li')
    # goods=bro.find_elements_by_class_name('gl-item')
    goods = bro.find_elements_by_css_selector('.gl-item')
    # print(len(goods))
    for good in goods:
        try:
            price = good.find_element_by_css_selector('.p-price i').text
            name = good.find_element_by_css_selector('.p-name em').text
            url = good.find_element_by_css_selector('.p-img a').get_attribute('href')
            commits = good.find_element_by_css_selector('.p-commit strong>a').text
            photo_url = good.find_element_by_css_selector('.p-img img').get_attribute('src')

            print('''
            商品名字：%s
            商品价格：%s
            商品地址：%s
            商品评论数：%s
            商品图片地址：%s
    
            ''' % (name, price, url, commits, photo_url))
        except Exception as e:
            continue

    next_button = bro.find_element_by_partial_link_text('下一页')
    time.sleep(1)
    next_button.click()

    get_goods_info(bro)





try:
    bro.get('https://www.jd.com/')

    input_k=bro.find_element_by_id('key')

    input_k.send_keys('奶牛')
    # 模拟键盘的回车键
    input_k.send_keys(Keys.ENTER)
    get_goods_info(bro)


except Exception as e:
    print(e)

finally:
    bro.close()
