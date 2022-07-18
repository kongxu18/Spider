# 已经没有web网页了
import requests
from bs4 import BeautifulSoup

ret = requests.get('https://qiushibaike.com/text/page/2')
print(ret.encoding)
ret.encoding='utf8'
print(ret.text)
soup = BeautifulSoup(ret.text,'html.parser')

article_list = soup.find_all(class_='article')

for article in article_list:
    content = article.find(class_='content').text
    print(content)