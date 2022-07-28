import scrapy
from bs4 import BeautifulSoup
from lxml import etree
from scrapy.http.request import Request
from firstscrapy.items import ChoutiItem


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response, **kwargs):
        """
        使用自带的解析
        持久化：2.使用pipeline item 存储 保存到mysql
        终端 运行 scrapy crawl chouti -o chouti.csv
        :return: item对象
        """
        # title = response.css('.link-title')
        # .extract() 把对象的值取出来
        # 解析出所有标题，图片，地址
        print(response.headers)
        divs = response.xpath('//div[contains(@class,"link-item")]')
        for div in divs:
            item = ChoutiItem()
            # a_list = div.xpath('//a[contains(@class,"link-title")]')
            title: str = div.css('.link-title::text').extract_first()
            url = div.css('.link-title::attr(href)').extract_first()
            pic_url = div.css('.image-scale::attr(src)').extract_first()
            title = title.replace('\u200b', '')
            # print(repr(title))
            item['title'] = title
            item['url'] = url
            item['pic_url'] = pic_url if pic_url else ''
            yield item

    def parse5(self, response, **kwargs):
        """
        使用自带的解析
        持久化：1.保存到本地文件
        终端 运行 scrapy crawl chouti -o chouti.csv
        -o 代表 output
        """
        li = []
        # title = response.css('.link-title')
        # .extract() 把对象的值取出来
        # 解析出所有标题，图片，地址
        divs = response.xpath('//div[contains(@class,"link-item")]')
        for div in divs:
            # a_list = div.xpath('//a[contains(@class,"link-title")]')
            title = div.css('.link-title::text').extract_first()
            url = div.css('.link-title::attr(href)').extract_first()
            pic_url = div.css('.image-scale::attr(src').extract_first()
            li.append({'title': title, 'url': url, 'pic_path': pic_url})
            return li

    def parse4(self, response, **kwargs):
        """
        在使用 xpath ，for 循环遍历 selector_list 对象时候，会自动返回原本的xpath解析对象的顶层
        重新开始解析，需用使用 . 表示针对当前循环的内容进行解析
        """

        divs = response.xpath('//div[contains(@class,"link-item")]')
        for div in divs:
            a = div.xpath('.//a[contains(@class,"link-title")]')[0]
            title = a.xpath('./text()').extract()[0]
            url = a.xpath('./@href').extract()[0]

            print(title, url)

    def parse2(self, response, **kwargs):
        # 如果此时又解析出一个url，想进行爬取其他网址
        # 不进行去重 ， 此时这么写会进入一个死循环
        return Request('https://www.baidu.com', dont_filter=True)

    def parse3(self, response, **kwargs):
        """
        自己解析 low
        :param response:
        :param kwargs:
        :return:
        """
        # print(response.text)
        # 解析数据
        html = etree.HTML(response.text)
        a_list = html.xpath('//a[contains(@class,"link-title")]')
        print(len(a_list))
        for a in a_list:
            print(a.text)

        return
