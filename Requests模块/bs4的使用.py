from bs4 import BeautifulSoup

# 文档容错能力，解析的内容可能不是一个正确的html标签
html_doc ="""
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

soup = BeautifulSoup()