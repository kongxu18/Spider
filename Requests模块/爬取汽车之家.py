import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.autohome.com.cn/news/1/#liststart')

# 第二个参数：使用什么解析器,html.parser 内资解析器
# lxml Html解析器 需要安装
soup = BeautifulSoup(res.text, 'lxml')
ul_list = soup.find_all(class_='article')
print(len(ul_list))

# 继续找ul下的所有li标签
for ul in ul_list:
    li_list = ul.find_all(name='li')
    for li in li_list:
        title = li.find(name='h3')
        if title:
            title = title.text
            url = 'https:'+li.find('a').attrs.get('href')
            desc = li.find('p').text
            img = li.find('img')['src']
            if 'https' not in img:
                img = 'https:' + img
        print(img)
# print(len(li_list))