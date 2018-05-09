# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuRoomItem
from douyuSpider.sqlhelper import MysqlHelper
from douyuSpider.autocreatedb import CreateDB


class DouyulolSpider(scrapy.Spider):
    name = 'douyulol'
    allowed_domains = ['open.douyucdn.cn']
    offset = 0
    db = CreateDB()
    shoretnames = db.getShortName()
    for shortname in shoretnames:
        shortname = shortname[0]
        url = "http://open.douyucdn.cn/api/RoomApi/live/"+shortname+"?limit=20&offset="
        start_urls = [url + str(offset)]

    def parse(self, response):
        loldatas = json.loads(response.text)['data']
        #filename = 'daouyumess.txt'
        #print(loldatas)
        #open(filename,'wb+').write(loldatas)
        for data in loldatas:
            item = DouyuRoomItem()

            item['room_id'] = data['room_id']
            item['owner_uid'] = data['owner_uid']
            item['nickname'] = data['nickname']
            item['url'] = data['url']
            item['shortname']=self.shortname
            #print(item['shortname'])
            #open(filename,'a+').write(str(item['room_id'])+'\n')
            yield item
        if self.offset <= 200:
            self.offset += 20
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)
        else:
            return

