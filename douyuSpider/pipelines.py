# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from . sqlhelper import MysqlHelper
from .items import DouyuspiderItem, DouyuRoomItem


class DouyuspiderPipeline(object):
    def __init__(self):
        host = settings['MYSQL_HOST']
        port = settings['MYSQL_PORT']
        daname = settings['MYSQL_DBNAME']
        tablename = settings['MYSQL_TABLE']
        user = settings['MYSQL_USER']
        password = settings['MYSQL_PASSWORD']
        self.mysqlhelper = MysqlHelper(host, port, daname, user, password)

    def process_item(self, item, spider):
        parames = item['room_id']
        shortname = item['shortname']
        #filename = 'roomid.txt'
        #open(filename,'a+').writelines(str(item['room_id'])+'\n')
        #return item
        sql = """select * from """+shortname+""" where room_id = %s;"""
        ret = self.mysqlhelper.get_one(sql, parames)
        if ret:
            sql = 'update '+shortname+' set nickname = %s where room_id = %s;'
            params = [item['nick_name'], item['room_id']]
            self.mysqlhelper.update(sql, params)
            return item
        else:
            sql = 'insert into '+shortname+'(room_id,owner_uid,nickname,url) VALUES (%s,%s,%s,%s);'
            params = [item['room_id'], item['owner_uid'], item['nickname'], item['url']]
            self.mysqlhelper.insert(sql, params)
            return item
