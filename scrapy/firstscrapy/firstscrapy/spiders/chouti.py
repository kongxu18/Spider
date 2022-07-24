import scrapy
from bs4 import BeautifulSoup
from lxml import etree
from scrapy.http.request import Request

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response, **kwargs):
        """

        :param response:
        :param kwargs:
        :return:
        """
        # print(response.text)
        # 解析数据
        html = etree.HTML(response.text)
        # 解析出一个网址，需要继续爬取
        a_list = html.xpath('//a[contains(@class,"link-title")]')

        return Request

    # def parse(self, response,**kwargs):
    #     """
    #     自己解析 low
    #     :param response:
    #     :param kwargs:
    #     :return:
    #     """
    #     # print(response.text)
    #     # 解析数据
    #     html = etree.HTML(response.text)
    #     a_list = html.xpath('//a[contains(@class,"link-title")]')
    #     print(len(a_list))
    #     for a in  a_list:
    #         print(a.text)
    #
    #     return
