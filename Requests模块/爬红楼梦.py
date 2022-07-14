import requests
from bs4 import BeautifulSoup
import time
import urllib3
urllib3.disable_warnings()
ret = requests.get('https://www.shicimingju.com/book/hongloumeng.html',verify=False)
ret.encoding = 'utf8'

soup = BeautifulSoup(ret.text, 'lxml')
li_list = soup.find(class_='book-mulu').find('ul').find_all('li')

with open('红楼梦.txt', 'w', encoding='utf8') as f:
    for li in li_list:
        content = li.find('a').text
        url = 'https://www.shicimingju.com' + li.find('a').get('href')
        try:
            f.write(content)
            f.write('\n')
        except Exception as err:
            print(content, 'wrong', err)

        n = 0
        while True:
            print(n,url)
            res_content = requests.get(url,verify=False)

            res_content.encoding = 'utf8'
            print(res_content.encoding)

            if res_content.status_code == 200:
                soup2 = BeautifulSoup(res_content.text, 'lxml')
                article = soup2.find(class_='chapter_content').text
                f.write(article)
                f.write('\n')
                print(content, '写入')
                break
            n +=1


        time.sleep(3)
