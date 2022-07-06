import requests

html = requests.get('https://www.mzitu.com')
print(html.text)

# 图片防盗链
# 请求头带 referer
