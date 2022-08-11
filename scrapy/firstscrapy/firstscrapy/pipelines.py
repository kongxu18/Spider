# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

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
        self.file.write(item['pic_url'] + '\n')

        return item

    def close_spider(self,spider):
        """
        结束调用
        :return:
        """
        self.file.close()


class ChoutiMysqlPipeline:
    def open_spider(self, spider):
        """
        首次调用
        :param spider:
        :return:
        """
        self.conn = pymysql.connect(host='127.0.0.1',
                                    user='root',password='root',
                                    database='chouti',port=3306)
    def close_spider(self,spider):
        self.conn.close()


    def process_item(self, item, spider):
        curser = self.conn.cursor()
        sql = 'insert into article(title,url,pic_url)values (%s,%s,%s)'
        title : str= item['title']
        title = title.strip()
        curser.execute(sql,[title,item['url'],item['pic_url']])
        self.conn.commit()
        return item


