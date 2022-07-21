import requests

session = requests.session()
data = {
    'username': '2728559633@qq.com',
    'password': '333333a',
    'captcha': '2dch',
    'remember': '1',
    'ref': 'http://www.aa7a.cn/user.php?act=logout',
    'act': 'act_login'
}
rest = session.post('http://www.aa7a.cn/user.php', data=data)
print(rest.text)
# cookie
cookie = rest.cookies

print('--------------------')
# 携带cookie
# rest1 = requests.get('http://www.aa7a.cn/index.php',cookies=cookie)
rest2 = session.get('http://www.aa7a.cn/index.php')
print('2728559633@qq.com' in rest2.text)