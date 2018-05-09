#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 11:43
# @Author  : huanghe
# @Site    : 
# @File    : autocreatedb.py
# @Software: PyCharm
from scrapy.conf import settings
from douyuSpider.sqlhelper import MysqlHelper
class CreateDB(object):
    def __init__(self):
        host = settings['MYSQL_HOST']
        port = settings['MYSQL_PORT']
        daname = settings['MYSQL_DBNAME']
        tablename = settings['MYSQL_TABLE']
        user = settings['MYSQL_USER']
        password = settings['MYSQL_PASSWORD']
        self.mysqlhelper = MysqlHelper(host, port, daname, user, password)

    def createDB(self):
        sql = 'SELECT short_name from all_game ORDER BY cate_id ASC;'
        datas = self.mysqlhelper.get_all(sql)
        # print(datas)
        for data in datas:
            creataql = '''CREATE TABLE ''' + data[0] + '''(
                              `id`  int(11) NOT NULL AUTO_INCREMENT ,
                              `room_id`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
                              `owner_uid`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
                              `nickname`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
                              `url`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
                              PRIMARY KEY (`id`)
                              );'''
            #print(creataql)
            self.mysqlhelper.create(creataql)
    def getShortName(self):
        sql = 'SELECT short_name from all_game ORDER BY cate_id ASC;'
        datas = self.mysqlhelper.get_all(sql)
        return datas


if __name__ == '__main__':
    db = CreateDB()
    db.createDB()

