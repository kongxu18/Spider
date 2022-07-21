import requests

# 1 发送get请求
# res是python的对象，对象里，响应头，响应体。。。。
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
#     'referer': 'https://www.mzitu.com/225078/2'
# }
# # res = requests.get('https://www.mzitu.com/', headers=header)
# # print(res.text)
# res1 = requests.get('https://i3.mmzztt.com/2020/03/14a02.jpg', headers=header)
# print(res1.text)
# # print(res1.content)  # 二进制内容
#
# with open('a.jpg', 'wb')as f:
#     for line in res1.iter_content():
#         f.write(line)


# 2 请求地址中携带数据(两种方式，推荐第二种)

# from urllib.parse import urlencode,unquote  # url的编码和解码
# print(unquote('%E7%BE%8E%E5%A5%B3'))
# %E7%BE%8E%E5%A5%B3
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
# }
# # res=requests.get('https://www.baidu.com/s?wd=美女',headers=header)
# res=requests.get('https://www.baidu.com/s',headers=header,params={'wd':'美女'})
# print(res.url)
# print(res.text)

# 3 请求带cookie(两种方式)
# 方式一，在header中放
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
#     'cookie':'key=asdfasdfasdfsdfsaasdf;key2=asdfasdf;key3=asdfasdf'
# }
# res=requests.get('http://127.0.0.1:8000/index/',headers=header)
# 方式二：
# header = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
# }
# # cookies是一个字典或者CookieJar对象
# res=requests.get('http://127.0.0.1:8000/index/',headers=header,cookies={'key':'asdfasdf'})
# print(res.text)
# 问：你的网站从哪取出cookie来


# 4 发送post请求，携带数据（urlencoded和json）
# res=requests.post('http://127.0.0.1:8000/index/',data={'name':'lqz'})
# print(res.text)

# res=requests.post('http://127.0.0.1:8000/index/',json={'age':1,},)
# print(res.text)


# 5 自动携带cookie
# session=requests.session()
# res=session.post('http://127.0.0.1:8000/index/')  # 假设这个请求登录了
# res1=session.get('http://127.0.0.1:8000/order/')  # 现在不需要手动带cookie，session会帮咱处理

# 6 response对象
# respone=requests.post('http://127.0.0.1:8000/index/',data={'name':'lqz'})
# # print(respone.text)  # 响应的文本
# print(respone.content)  # 响应体的二进制
#
#
# print(respone.status_code)  # 响应状态码
# print(respone.headers)    # 响应头
# print(respone.cookies)   # cookie
# print(respone.cookies.get_dict()) #  把cookie转成字典
# print(respone.cookies.items())  # key和value
#
# print(respone.url)        # 请求的url
# print(respone.history)   #[]放重定向之前的地址
#
# print(respone.encoding)  # 响应的编码方式

# respone.iter_content()  # 图片，视频，大文件，一点一点循环取出来
# for line in respone.iter_content():
#     f.write(line)

# 7 编码问题
res=requests.get('http://www.autohome.com/news')
# # 一旦打印出来出现乱码问题
# # 方式一
res.encoding='gb2312'
# # 方式二
# res.encoding=res.apparent_encoding
# print(res.text)


# 8 解析json
# import json
# respone=requests.post('http://127.0.0.1:8000/index/',data={'name':'lqz'})
# # print(type(respone.text))  # 响应的文本
# # print(json.loads(respone.text))
# print(respone.json())  # 相当于上面那句话
# print(type(respone.json()))  # 相当于上面那句话


# 9 高级用法之ssl（了解）
# import requests
# respone=requests.get('https://www.12306.cn') #不验证证书,报警告,返回200
# print(respone.status_code)
# 使用证书，需要手动携带

# import requests
# respone=requests.get('https://www.12306.cn',
#                      cert=('/path/server.crt',
#                            '/path/key'))
# print(respone.status_code)

# 10 高级用法：使用代理

# respone=requests.get('http://127.0.0.1:8000/index/',proxies={'http':'代理的地址和端口号',})
# 代理，免费代理，收费代理花钱买
# 代理池：列表放了一堆代理ip，每次随机取一个，再发请求就不会封ip了
# 高匿和透明代理？如果使用高匿代理，后端无论如何拿不到你的ip，使用透明，后端能够拿到你的ip
# 后端如何拿到透明代理的ip，  后端：X-Forwarded-For
# respone=requests.get('https://www.baidu.com/',proxies={'http':'27.46.20.226:8888',})
# print(respone.text)


# 11 超时设置
# import requests
# respone=requests.get('https://www.baidu.com',
#                      timeout=0.0001)


# 12 认证设置（你见不到了）
# import requests
# r=requests.get('xxx',auth=('user','password'))
# print(r.status_code)


# 13 异常处理
# import requests
# from requests.exceptions import * #可以查看requests.exceptions获取异常类型
#
# try:
#     r=requests.get('http://www.baidu.com',timeout=0.00001)
# # except ReadTimeout:
# #     print('===:')
# except Exception as e:
#     print(e)


# 14 上传文件
# res=requests.post('http://127.0.0.1:8000/index/',files={'myfile':open('a.jpg','rb')})
# print(res.text)


# 模拟登录某网站
# import requests
#
# data = {
#     'username': '616564099@qq.com',
#     'password': 'lqz123',
#     'captcha': 'zdu4',
#     'remember': 1,
#     'ref': 'http://www.aa7a.cn/user.php?act=logout',
#     'act': 'act_login',
# }
# rest = requests.post('http://www.aa7a.cn/user.php',data=data)
# print(rest.text)
# # 拿到cookie
# cookie=rest.cookies
# print(cookie)
#
# # 携带着cookies，表示登录了，页面中会有我们的用户信息616564099@qq.com
# rest1=requests.get('http://www.aa7a.cn/index.php',cookies=cookie)
# # rest1=requests.get('http://www.aa7a.cn/index.php')
# print('616564099@qq.com' in rest1.text)


# import requests
# session=requests.session()
# data = {
#     'username': '616564099@qq.com',
#     'password': 'lqz123',
#     'captcha': 'zdu4',
#     'remember': 1,
#     'ref': 'http://www.aa7a.cn/user.php?act=logout',
#     'act': 'act_login',
# }
# rest = session.post('http://www.aa7a.cn/user.php',data=data)
# print(rest.text)
# # 拿到cookie
# cookie=rest.cookies
# print(cookie)
#
# # 携带着cookies，表示登录了，页面中会有我们的用户信息616564099@qq.com
# rest1=session.get('http://www.aa7a.cn/index.php')
# # rest1=requests.get('http://www.aa7a.cn/index.php')
# print('616564099@qq.com' in rest1.text)



# 爬取梨视频
import requests
import re

res=requests.get('https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=1&start=0')

# print(res.text)
re_video='<a href="(.*?)" class="vervideo-lilink actplay">'
video_urls=re.findall(re_video,res.text)
# https://www.pearvideo.com/
# print(video_urls)

for video in video_urls:
    url='https://www.pearvideo.com/'+video
    print(url)
    # 向视频详情发送get请求
    res_video=requests.get(url)
    # print(res_video.text)
    # break
    re_video_mp4='hdUrl="",sdUrl="",ldUrl="",srcUrl="(.*?)",vdoUrl=srcUrl,skinRes'
    video_url=re.findall(re_video_mp4,res_video.text)[0]
    print(video_url)
    video_name=video_url.rsplit('/',1)[-1]
    print(video_name)
    res_video_content=requests.get(video_url)
    with open(video_name,'wb') as f:
        for line in res_video_content.iter_content():
            f.write(line)
