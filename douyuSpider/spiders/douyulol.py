# -*- coding: utf-8 -*-
import scrapy
import json
from douyuSpider.items import DouyuRoomItem


class DouyulolSpider(scrapy.Spider):
    name = 'douyulol'
    allowed_domains = ['http://open.douyucdn.cn']
    offset = 0
    url = "http://open.douyucdn.cn/api/RoomApi/live/1?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        loldatas = json.loads(response.text)['data']
        filename = 'daouyumess.txt'
        print(loldatas)
        #open(filename,'wb+').write(loldatas)
        '''for data in loldatas:
            item = DouyuRoomItem()
            item['room_id'] = data['room_id']
            item['ower_uid'] = data['ower_uid']
            item['nickname'] = data['nickname']
            item['url'] = data['url']
            yield item
        if self.offset <= 200:
            self.offset += 20
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
        else:
            return'''

