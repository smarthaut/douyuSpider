#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 15:40
# @Author  : huanghe
# @Site    : 
# @File    : sqlhelper.py
# @Software: PyCharm
import pymysql

class MysqlHelper:
    def __init__(self,host='localhost',port=3306,db='test2',user='root',passwd='mysql',charset='utf8'):
        self.conn=pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset=charset)
        self.cursor = self.conn.cursor()

    def insert(self,sql,params):
        self.cursor.execute(sql,params)
        self.conn.commit()

    def update(self,sql,params):
        self.cursor.execute(sql,params)
        self.conn.commit()

    def delete(self,sql,params):
        self.cursor.execute(sql,params)
        self.conn.commit()
