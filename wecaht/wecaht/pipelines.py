# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymysql import connections

class WecahtPipeline(object):

    def __init__(self):

        self.conn = pymysql.connect(host='127.0.0.1',user='root',passwd='990619',db='wechat',charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        name = item['name']
        texts = item['texts']
        sql = "insert into wechat1(name,texts) VALUES(%s,%s)"
        self.cursor.execute(sql,(name,texts))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()