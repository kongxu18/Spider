import requests

# 实际要爬取的url
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

payload = {
    'first': 'true',
    'pn': '1',
    'kd': 'python',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
Cookie = 'user_trace_token=20220718225230-e17b37e0-c58d-4212-aaea-0aa5527f5701; X_HTTP_TOKEN=72c22169a10bcfe20595518561fc01ed69d58225dc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1658155951; _ga=GA1.2.348583840.1658155951; LGSID=20220718225230-6c0a37a1-aab0-43be-8ea8-dcd8730d6a19; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https://www.baidu.com/other.php?sc.a00000ateDFHTxzs6deF1lRtbb1OgAOdJNQh28pXzhuxb3SGZZ44RoYQumotZzQqKFC9LkPgVKJhxt-TENJMbdOJYeh94hlrDz9depMm-zGF5ohcl0jgsLclZ8aORJTmSYfWKY9SRUozGr5j3Wd_jBCtmyeYLdpfOe1-8MbP7I9dzkob9aNigjdXARcvDlPm30HsNuFE_55YyZnoWlveuvdB9W-r.7Y_NR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt_rE-9kYryqM764TTPqKi_nYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4V0KdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujL0oUhY0ZFWIWYs0ZNzU7qGujYkPHn3rH0Yrjf30Addgv-b5HDYrHnLPHc40AdxpyfqnHDLn164PHD0UgwsU7qGujYknW6zP6KsI-qGujYs0A-bm1dribGH0ZKGujYz0APGujYYnjR0mLFW5Hfzrj61&dt=1658155947&wd=%E6%8B%89%E5%8B%BE&tpl=tpl_12826_28972_0&l=1538904848&us=linkVersion%3D1%26compPath%3D10036.0-10032.0%26label%3D%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%2598%26linkType%3D%26linkText%3D%25E3%2580%2590%25E6%258B%2589%25E5%258B%25BE%25E6%258B%259B%25E8%2581%2598%25E3%2580%2591%25E5%25AE%2598%25E6%2596%25B9%25E7%25BD%2591%25E7%25AB%2599%2520-%2520%25E4%25BA%2592%25E8%2581%2594%25E7%25BD%2591%25E9%25AB%2598%25E8%2596%25AA%25E5%25A5%25BD%25E5%25B7%25A5; PRE_LAND=https://www.lagou.com/landing-page/pc/search.html?utm_source=m_cf_cpt_baidu_pcbt; LGUID=20220718225230-2b0987ae-9275-4e78-856a-074a9122512a; sajssdk_2015_cross_new_user=1; _gid=GA1.2.1258169330.1658157089; gate_login_token=77826ba5a56357ba6d675339c1485fa18a19ed1be5cfe254e2ad435ff3b7cfd2; LG_LOGIN_USER_ID=0975c156a155572256a48ace519732515c386b015ec82db43267daaec1100224; LG_HAS_LOGIN=1; _putrc=13DEF8900AC05C10123F89F2B170EADC; JSESSIONID=ABAAAECABFAACEAF4AEBD99BE96E2053532D1615F4609CE; login=true; unick=子华; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; WEBTJ-ID=20220718231214-18211ddf31b820-0c32393813d26f-594f2612-3686400-18211ddf31c814; RECOMMEND_TIP=true; _gat=1; __SAFETY_CLOSE_TIME__14904134=1; sensorsdata2015session={}; index_location_city=上海; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1658157138; TG-TRACK-CODE=index_search; LGRID=20220718231250-15e6dbf2-6179-4e4b-a694-f601f31a4814; __lg_stoken__=ff2a4f9cdf5fe600042f725ea866687cf9c937a48d4173fd97413a2d18b0953c730865dacd01997f3ed3a5276376996805b703c74d46e4ddd9af684b0c16d199d693fa7d6552; sensorsdata2015jssdkcross={"distinct_id":"14904134","$device_id":"18211dd3ed7a01-0dcb031f63a948-594f2612-3686400-18211dd3ed814f","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$os":"Windows","$browser":"Chrome","$browser_version":"97.0.4692.71"},"first_id":"18211dd3ed7a01-0dcb031f63a948-594f2612-3686400-18211dd3ed814f"}'
Cookie = Cookie.encode('utf8')
# print(Cookie)
header['Cookie'] = Cookie
# 原始的url
urls = 'https://www.lagou.com/jobs/list_python/p-city_3?&cl=false&fromSearch=true&labelWords=&suginput='
# 建立session
s = requests.Session()
# 获取搜索页的cookies
s.get(urls, headers=header, timeout=3)
# 为此次获取的cookies
cookie = s.cookies
# 获取此次文本
response = s.post(url, data=payload, headers=header, cookies=cookie, timeout=5)
response.encoding = 'utf8'
print(response.text)
