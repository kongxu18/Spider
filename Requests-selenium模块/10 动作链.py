from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# ActionChains(driver).click_and_hold(sourse)
# ActionChains(driver).move_by_offset  :移动x轴和y轴的拒绝
# ActionChains(driver).move_to_element() ：直接移动到某个控件是上
# ActionChains(driver).move_to_element_with_offset() #移动到某个控件的某个位置
# ActionChains(driver).release()
# 所有的动作最后都要执行perform()，真正的去执行
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.implicitly_wait(3)  # 使用隐式等待

try:
    driver.switch_to.frame('iframeResult') ##切换到iframeResult
    sourse=driver.find_element_by_id('draggable')
    target=driver.find_element_by_id('droppable')
    ActionChains(driver).click_and_hold(sourse).perform()
    distance=target.location['x']-sourse.location['x']

    track=0
    while track < distance:
        ActionChains(driver).move_by_offset(xoffset=20,yoffset=0).perform()


        track+=20
    # 释放动作链
    ActionChains(driver).release().perform()

    time.sleep(10)


finally:
    driver.close()