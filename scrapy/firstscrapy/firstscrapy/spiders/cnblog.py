import scrapy
from firstscrapy.items import CnblogsItem
from scrapy import Request
from scrapy.http.request import Request


class CnblogSpider(scrapy.Spider):
    name = 'cnblog'
    allowed_domains = ['www.cnblogs.com']
    start_urls = ['http://www.cnblogs.com/']

    def parse(self, response, **kwargs):
        # print(response.text)
        div_list = response.css('article.post-item')

        for div in div_list:
            item = CnblogsItem()
            title = div.xpath('.//div[1]/a/text()').extract_first()
            url = div.xpath('.//div[1]/a/@href').extract_first()
            desc = div.xpath('.//div/p/text()').extract()
            desc = ''.join(desc).strip()
            item['title'] = title
            item['url'] = url
            item['desc'] = desc
            # 继续爬取详情
            # callback 如果不写，默认回调到pares
            # 写了回调函数，就会回到写的函数内
            yield Request(url, callback=self.parse_detail,meta={'item':item})

    def parse_detail(self, response, **kwargs):
        content = response.css('#cnblogs_post_body').extract_first()
        item = response.meta.get('item')
        item['content'] = content