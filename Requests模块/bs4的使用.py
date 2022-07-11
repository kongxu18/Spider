from bs4 import BeautifulSoup

# 文档容错能力，解析的内容可能不是一个正确的html标签
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p id="my_p" class="title">hello<b id="bbb" class="boldest">The Dormouse's story</b>
</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')
# 美化 html代码
# print(soup.prettify())

# 遍历文档树
# 解释：即直接通过标签名字选择，特点是速度快，如果存在多个相同的标签则只返回第一个
# 1.用法
head = soup.head
print(head)

# 2.获取标签的名字
print(head.name)

# 3.获取标签的属性
p = soup.body.p
# class 可能有多个，就放入列表中
print(p.attrs, p.get('class'))

# 4.获取标签的内容:会获取所有的子标签内容
print(p.text)
# p 下的文本只有一个才能取到，否则任何情况都是none
print(p.string)
# strings：返回一个包含所有内容的生成器
print(p.strings)

# 5.嵌套选择
a = soup.body.a

# 6.子节点，子孙节点:两者获取结果一样，一个返回列表，一个返回生成器
children = soup.p.contents
children_ = soup.p.children

# 7.父节点，祖先节点
par = soup.a.parent  # 只有一个父节点
par_ = soup.a.parents  # 所有父节点
print('---------------')
print(par, '///', par_)

# 8.兄弟节点
bro1 = soup.a.next_sibling  # 下一个兄弟
bro1_ = soup.a.next_siblings
bro2 = soup.a.previous_silbling  # 上一个兄弟
bro2_ = soup.a.previous_silblings
print('---------------')
print(bro1)

"""
搜索文档树
"""
# find 只返回找到的第一个
# find_all  找到所有
# 5种过滤器：字符串，正则表达式，列表，True，方法

# 字符串过滤:过滤内容是字符串
# soup.find(name='a')
# soup.find(id ='my_p')
res = soup.find(attrs={'id': 'my_p', 'class': 'title'})
print('---------------')
print(res)

# 正则表达式：过滤内容是正则表达式
import re

pattern = re.compile('^b')
res1 = soup.find_all(name=pattern)  # 查找所有以b开头的所有标签
res2 = soup.find_all(id=re.compile('^l'))
print(res2)

# 列表匹配：过滤内容是列表
res = soup.find_all(name=['body', 'b'])
print('-----------------')
print(res)

# True 和 False
res = soup.find_all(id=True)  # 找所有都有id属性的


# 方法
def has_class_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


res = soup.find_all(has_class_no_id)

# limit 参数限制条数

# recursive 参数 默认True 递归查找,寻找子子孙孙；False 不递归，只找第一层
