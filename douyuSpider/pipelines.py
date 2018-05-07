# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from douyuSpider.sqlhelper import MysqlHelper

class DouyuspiderPipeline(object):

    def __init__(self):
        host = settings['MYSQL_HOST']
        port = settings['MYSQL_PORT']
        daname = settings['MYSQL_DBNAME']
        tablename = settings['MYSQL_TABLE']
        user = settings['MYSQL_USER']
        password = settings['MYSQL_PASSWORD']
        self.mysqlhelper = MysqlHelper(host,port,daname,user,password)

    def process_item(self,item, spider):
        params = [item['cate_id'],item['game_name'],item['short_name'],item['game_url'],item['game_src'],
                  item['game_icon']]
        sql = 'insert into all_game(cate_id,game_name,short_name,game_url,game_src,game_icon) values(%s,' \
              '%s,%s,%s,%s,%s);'
        self.mysqlhelper.insert(sql,params)
        return item
