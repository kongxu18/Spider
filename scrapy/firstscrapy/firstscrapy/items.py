# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChoutiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    pic_url = scrapy.Field()


class CnblogsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    content = scrapy.Field()