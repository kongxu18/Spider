import requests
from lxml import etree
import datetime

# 评论


with open("cookie.txt", "r", encoding="utf-8") as f:
    cookie = f.read()

lick_url = "https://dig.chouti.com/link/vote"
header_dict = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "15",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": f"{cookie}",
    "Host": "dig.chouti.com",
    "Origin": "https://dig.chouti.com",
    "Referer": "https://dig.chouti.com/",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
# ret = requests.get('https://dig.chouti.com/', headers=header_dict)
# print(ret.text)

# 前25条是静态网页，后25天js动态加载
# 拿取所有新闻的id号
# html = etree.HTML(ret.text)
# id_list = html.xpath('//div[@class="link-detail"]/a[contains(@class,"link-title")]/@data-id')
# print(id_list)

# 再获取动态加载的25条，经过对js动态加载的链接进行试验，发现最开始的25条新闻的请求url
# 首先获取当前时间戳
now_time = datetime.datetime.now().timestamp() * 1000
now_time = str(now_time)[0:13]


def get_id(url, arg):
    res_list = []
    res_json = requests.get(url=url, headers=header_dict)

    for data in res_json.json()['data']:
        id_ = data.get('id')
        res_list.append(id_)
        # 获取最后一个文章的operateTime，作为拼接下一个请求的参数
        arg['operateTime'] = data.get('operateTime')
    return res_list


arg = {'operateTime': ''}
# 拼接url https://dig.chouti.com/link/hot?afterTime=1659247205019000&_=1659276229763
url = "https://dig.chouti.com/link/hot?afterTime=&_=%s" % now_time

# id_list_24 = get_id(url, arg)
# print(id_list_24)
url = "https://dig.chouti.com/link/hot?afterTime=%s&_=%s" % (arg['operateTime'], now_time)

# id_list_49 = get_id(url, arg)
# print(id_list_49)

# id_set = set(id_list_24) | set(id_list_49)
# print(id_set)
# print(len(id_set))

# 获取到前面50条文章id以后就可以进行评论了 https://dig.chouti.com/comments/create


"""
登陆返回的cookie 无用

"""

# 评论每日有限制。先点赞
for id_ in [0]:
    # data = {'content': "哈哈哈,我来评论了", 'linkId': id_,
    #         'parentId': "0", 'pictureUrl': "", "subjectId": "1"}
    # data = {'linkId': id_}
    argument = requests.post('https://dig.chouti.com/link/vote', headers=header_dict, cookies=cookie,
                             data={'linkId': "35838202"})
    print(argument.text)
    break
