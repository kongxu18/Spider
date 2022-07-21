"""
拉勾网更新
全部加密以后利用request 不好爬取了

"""

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

    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/',
    # 'sec-ch-ua': ' ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}
cookie = 'JSESSIONID=ABAAABAABAGABFAB346378AD92BAFD4909681926BEBB659; WEBTJ-ID=20220721001155-1821c614f59224-02a600bcee3007-c4e7526-3686400-1821c614f5ac05; RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1658333516; user_trace_token=20220721001155-96f4fa78-ceae-4290-bc13-78ca7bc03c07; LGUID=20220721001155-ff52a24c-295d-4f0e-931d-1c8dc1cce878; _ga=GA1.2.157383046.1658333516; sajssdk_2015_cross_new_user=1; sensorsdata2015session={}; _gid=GA1.2.1233213996.1658333516; privacyPolicyPopup=false; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=上海; __SAFETY_CLOSE_TIME__14904134=1; gate_login_token=f4f2def79ea2d74c74a175becc20be47f81d94412e50d3500aa1ed23133ab7b5; LG_LOGIN_USER_ID=bebbdec44d2e07db55e438008c18b682cdb24f5100f900e0b97d74344cf4de01; _putrc=13DEF8900AC05C10123F89F2B170EADC; login=true; unick=子华; TG-TRACK-CODE=index_search; __lg_stoken__=fd9cf185fc735ed3fe77f553a6a883be869056cd142934cd98a6609d8b842b5875a0c604660ba1402cf36e2d2865da284268994516d222bd9c9968b619c47cf997ab64ebceb5; X_MIDDLE_TOKEN=9dd9f0f14f68b3fdc807ec51be2a4c25; SEARCH_ID=4e22af981a774c719c723fee55a82f06; LGSID=20220721231449-a4fef42f-f892-48f6-b29f-1622d93d5617; PRE_UTM=; PRE_HOST=; PRE_SITE=https://www.lagou.com; PRE_LAND=https://www.lagou.com/; X_HTTP_TOKEN=78a2111f7a0ebc253137148561ef571fd44fdc2baa; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1658417314; LGRID=20220721232833-11b92d8e-ba19-45e9-9e75-0aa8e242dc8f; sensorsdata2015jssdkcross={"distinct_id":"14904134","first_id":"1821c61514e17c-06cd7122d89ee6-c4e7526-3686400-1821c61514fc27","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$os":"Windows","$browser":"Chrome","$browser_version":"103.0.0.0","lagou_company_id":""},"$device_id":"1821c61514e17c-06cd7122d89ee6-c4e7526-3686400-1821c61514fc27"}'
cookie = cookie.encode('utf8')
header['Cookie'] = cookie
# print(Cookie)
# 原始的url
urls = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# 建立session
s = requests.Session()
# 获取搜索页的cookies
s.get(urls, headers=header, timeout=3)
# 为此次获取的cookies
cookie = s.cookies
# 获取此次文本
response = s.post(url, headers=header, cookies=cookie, timeout=5)
response.encoding = 'utf8'
print(response.text)
