from gevent import monkey; monkey.patch_all()
import gevent.pool
import json
import random
import re

from lxml import etree
import execjs
import requests
# from sns_spider.config.settings import USER_AGENTS
# import pymongo


class LG(object):
    """拉钩 js逆向"""

    def __init__(self):
        # self.client = pymongo.MongoClient(host='localhost', port=27017)
        # self.mongo_col = self.client['demo']['lagou']
        self.js_file = open('lg.js', encoding='utf8').read()
        self._headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'referer': 'https://www.lagou.com/jobs/list_java/p-city_3?px=default',
        }
        self.token = ''
        self.proxies = dict()
        self.set_proxies()
        self.get_token()
        self.city_info = dict()
        self._headers['Cookie'] = 'JSESSIONID=ABAAABAABAGABFAB346378AD92BAFD4909681926BEBB659; WEBTJ-ID=20220721001155-1821c614f59224-02a600bcee3007-c4e7526-3686400-1821c614f5ac05; RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1658333516; user_trace_token=20220721001155-96f4fa78-ceae-4290-bc13-78ca7bc03c07; LGUID=20220721001155-ff52a24c-295d-4f0e-931d-1c8dc1cce878; _ga=GA1.2.157383046.1658333516; sajssdk_2015_cross_new_user=1; sensorsdata2015session={}; _gid=GA1.2.1233213996.1658333516; privacyPolicyPopup=false; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=上海; __SAFETY_CLOSE_TIME__14904134=1; gate_login_token=f4f2def79ea2d74c74a175becc20be47f81d94412e50d3500aa1ed23133ab7b5; LG_LOGIN_USER_ID=bebbdec44d2e07db55e438008c18b682cdb24f5100f900e0b97d74344cf4de01; _putrc=13DEF8900AC05C10123F89F2B170EADC; login=true; unick=子华; TG-TRACK-CODE=index_search; __lg_stoken__=fd9cf185fc735ed3fe77f553a6a883be869056cd142934cd98a6609d8b842b5875a0c604660ba1402cf36e2d2865da284268994516d222bd9c9968b619c47cf997ab64ebceb5; X_MIDDLE_TOKEN=9dd9f0f14f68b3fdc807ec51be2a4c25; SEARCH_ID=4e22af981a774c719c723fee55a82f06; LGSID=20220721231449-a4fef42f-f892-48f6-b29f-1622d93d5617; PRE_UTM=; PRE_HOST=; PRE_SITE=https://www.lagou.com; PRE_LAND=https://www.lagou.com/; X_HTTP_TOKEN=78a2111f7a0ebc253137148561ef571fd44fdc2baa; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1658417314; LGRID=20220721232833-11b92d8e-ba19-45e9-9e75-0aa8e242dc8f; sensorsdata2015jssdkcross={"distinct_id":"14904134","first_id":"1821c61514e17c-06cd7122d89ee6-c4e7526-3686400-1821c61514fc27","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$os":"Windows","$browser":"Chrome","$browser_version":"103.0.0.0","lagou_company_id":""},"$device_id":"1821c61514e17c-06cd7122d89ee6-c4e7526-3686400-1821c61514fc27"}'.encode('utf8')



    def set_proxies(self):
        """设置代理"""
        ip = "获取到代理IP"
        self.proxies = {
            'http': 'http://{}'.format(ip),
            'https': 'http://{}'.format(ip),
        }

    def get_response(self, url, params=None, data=None, method='GET'):
        while True:
            try:
                if method == 'GET':
                    response = requests.get(url, params=params, headers=self._headers)
                                            # proxies=self.proxies)
                else:
                    response = requests.post(url, params=params, data=data, headers=self._headers)
                    # proxies=self.proxies)
                response.encoding = response.apparent_encoding
                return response
            except:
                self.set_proxies()
                self.get_token()

    def get_token(self):
        """获取到游客cookie"""
        url = 'https://www.lagou.com/gongsi/allCity.html'
        while True:
            headers = self._headers

            try:
                response = requests.get(url, headers=headers, allow_redirects=False, timeout=10) # proxies=self.proxies
                response.encoding = response.apparent_encoding
                print(response.text)
                user_trace_token = re.findall(r'user_trace_token=(.*?);', response.headers['Set-Cookie'])[0]
                x_http_token = re.findall(r'X_HTTP_TOKEN=(.*?);', response.headers['Set-Cookie'])[0]
                href = response.headers['Location']

                ctx = execjs.compile(self.js_file, cwd='/opt/homebrew/Cellar/node/16.3.0/bin/')

                self.token = ctx.call('window.gt.prototype.a',
                                      json.dumps({"href": href, "search": href.split('check.html')[1]}))

                self._headers['cookie'] = 'user_trace_token={};X_HTTP_TOKEN={};__lg_stoken__={}'.format(
                    user_trace_token, x_http_token, self.token)
                return
            except Exception as e:
                # print('获取token失败\tproxies:{}\te:{}'.format(self.proxies, e))
                # self.set_proxies()
                # print(e)
                break

    def get_city_info(self):
        """获取城市信息"""
        url = 'https://www.lagou.com/jobs/allCity.html'
        html = etree.HTML(self.get_response(url).text)
        city_url = html.xpath('//ul[@class="city_list"]/li/a/@href')
        city_name = html.xpath('//ul[@class="city_list"]/li/a/text()')
        self.city_info = {city_name[i]: city_url[i] for i in range(len(city_url))}

    def get_job_info(self, input_item):
        """获取职位信息"""
        url = 'https://www.lagou.com/jobs/positionAjax.json'
        params = {
            "px": "default",
            "city": input_item['city_name'],
            "district": input_item['district'],
            "needAddtionalResult": "false",
        }
        sid = ''
        page = 1
        while True:
            data = {
                "first": "true",
                "pn": page,
                "kd": input_item['keyword'],
                "sid": sid,
            }
            job_info = self.get_response(url, params=params, data=data, method='POST').json()
            if 'success' in job_info:
                sid = job_info['content']['showId']
                job_info = job_info['content']['positionResult']['result']
                if not job_info or page == 30:
                    break
                self.parse_info(job_info, input_item)
                print('{}\t页码：{}\t数据量：{}'.format(input_item, page, len(job_info)))
            page += 1

    def parse_info(self, job_info, input_item):
        """解析内容"""
        items = list()
        for info in job_info:
            item = {
                '_id': info['positionId'],
                'job_name': info['positionName'],
                'job_url': 'https://www.lagou.com/jobs/{}.html'.format(info['positionId']),
                'company_name': info['companyFullName'],
                'company_size': info['companySize'],
                'industry_field': info['industryField'],
                'finance_stage': info['financeStage'],
                'company_label': info['companyLabelList'],
                'skill_label': info['skillLables'],
                'position_label': info['positionLables'],
                'create_time': info['createTime'],
                'city': info['city'],
                'district': info['district'],
                'salary': info['salary'],
                'work_year': info['workYear'],
                'job_nature': info['jobNature'],
                'education': info['education'],
                'position_advantage': info['positionAdvantage'],
                'position_detail': info['positionDetail'],
                'position_address': info['positionAddress']
            }
            items.append(item)
        try:
            self.mongo_col.insert_many(items)
            # print('{}\t插入成功。本次插入{}条'.format(input_item, len(items)))
        except:
            for item in items:
                try:
                    self.mongo_col.insert_one(item)
                except:
                    pass

    def run(self):
        """启动函数"""
        self.get_city_info()
        # print(self.city_info)
        # for city_name, city_url in self.city_info.items():
        for city_name in ['郑州', '北京', '上海', '广州', '深圳']:
            city_url = self.city_info[city_name]
            if '-zhaopin' not in city_url:
                city_url = city_url.rstrip('/') + '-zhaopin/'
            response = self.get_response(url=city_url, method='GET')
            html = etree.HTML(response.text)
            district_name = html.xpath('//div[@data-type="district"]/a[position()>1]/text()')
            item = [{'city_name': city_name, 'district': name, 'keyword': 'python'} for name in district_name]
            print(item)
            pool = gevent.pool.Pool(size=1)
            pool.map(self.get_job_info, item)


if __name__ == '__main__':
    t = LG()
    t.run()
