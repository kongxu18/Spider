"""
xpath 选择器使用
/ : 从根节点选取
// : 不管位置，直接找
"""

doc = '''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>div
   <a href='image1.html' aa='bb'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html' class='li li-item' name='items'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
   <a href='image6.html' name='items'><span><h5>test</h5></span>Name: My image 6 <br /><img src='image6_thumb.jpg' /></a>
  </div>
 </body>
</html>
'''
from lxml import etree

html = etree.HTML(doc)
# html=etree.parse('search.html',etree.HTMLParser())
# 1 所有节点
# a=html.xpath('//*')

# 2 指定节点（结果为列表）
# a=html.xpath('//head')

# 3 子节点，子孙节点
# a=html.xpath('//div/a')
# a=html.xpath('//body/a') #无数据
# a=html.xpath('//body//a')


# 4 父节点
# a=html.xpath('//body//a[@href="image1.html"]/..')
# a=html.xpath('//body//a[1]/..')
# 也可以这样
# a=html.xpath('//body//a[1]/parent::*')


# 5 属性匹配
# a=html.xpath('//body//a[@href="image1.html"]')

# 6 文本获取(重要)  /text() 取当前标签的文本
# a=html.xpath('//body//a[@href="image1.html"]/text()')
# a=html.xpath('//body//a/text()')

# 7 属性获取  @href 取当前标签的属性
# a=html.xpath('//body//a/@href')

# # 注意从1 开始取（不是从0）
# a=html.xpath('//body//a[1]/@href')
# 8 属性多值匹配
#  a 标签有多个class类，直接匹配就不可以了，需要用contains
# a=html.xpath('//body//a[@class="li"]')
# a=html.xpath('//body//a[contains(@class,"li")]')
# a=html.xpath('//body//a[contains(@class,"li")]/text()')

# 9 多属性匹配
# a=html.xpath('//body//a[contains(@class,"li") or @name="items"]')
# a=html.xpath('//body//a[contains(@class,"li") and @name="items"]/text()')
# a=html.xpath('//body//a[contains(@class,"li")]/text()')

# 10 按序选择
# a=html.xpath('//a[2]/text()')
# a=html.xpath('//a[2]/@href')

# 取最后一个
# a=html.xpath('//a[last()]/@href')

# 位置小于3的
# a=html.xpath('//a[position()<3]/@href')

# 倒数第二个
a = html.xpath('//a[last()-2]/@href')

# 11 节点轴选择

# ancestor：祖先节点
# 使用了* 获取所有祖先节点
# a=html.xpath('//a/ancestor::*')
# # 获取祖先节点中的div
# a=html.xpath('//a/ancestor::div')
# attribute：属性值
# a=html.xpath('//a[1]/attribute::*')
# a=html.xpath('//a[1]/@aa')
# child：直接子节点
# a=html.xpath('//a[1]/child::*')
# a=html.xpath('//a[1]/child::img/@src')
# descendant：所有子孙节点
# a=html.xpath('//a[6]/descendant::*')
# a=html.xpath('//a[6]/descendant::h5/text()')
# following:当前节点之后所有节点(兄弟节点和兄弟内部的节点)
# a=html.xpath('//a[1]/following::*')
# a=html.xpath('//a[1]/following::*[1]/@href')
# following-sibling:当前节点之后同级节点（只找兄弟）
# a=html.xpath('//a[1]/following-sibling::*')
# a=html.xpath('//a[1]/following-sibling::a')
# a=html.xpath('//a[1]/following-sibling::*[2]')
# a=html.xpath('//a[1]/following-sibling::*[2]/@href')


print(a)

# /
# //
# /@属性名
# /text()

