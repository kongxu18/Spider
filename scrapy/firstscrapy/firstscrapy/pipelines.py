# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ChoutiFilePipeline:
    """
    settings 里配置生效
    """
    def open_spider(self, spider):
        """
        首次调用
        :param spider:
        :return:
        """
        self.file = open('chouti.csv', 'w', encoding='utf8')

    def process_item(self, item, spider):
        self.file.write(item['title'] + '\n')
        self.file.write(item['url'] + '\n')
        self.file.write(item['pic_path'] + '\n')

        return item

    def close_spider(self):
        """
        结束调用
        :return:
        """
        self.file.close()


class ChoutiMysqlPipeline:
    def process_item(self, item, spider):
        print(item, 'mysql')
        return item
