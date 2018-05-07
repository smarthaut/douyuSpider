# -*- coding: utf-8 -*-
import scrapy
import json
from douyuSpider.items import DouyuspiderItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['http://open.douyucdn.cn/api/RoomApi/game']
    start_urls = ['http://open.douyucdn.cn/api/RoomApi/game']

    def parse(self, response):

        datas = json.loads(response.text)["data"]
        #filename = 'daouyumess.txt'
        #open(filename,'wb+').write(response.body)

        for data in datas:
            item = DouyuspiderItem()
            item['cate_id'] = data['cate_id']
            item['game_name'] = data['game_name']
            item['short_name'] = data['short_name']
            item['game_url'] = data['game_url']
            item['game_src'] = data['game_src']
            item['game_icon'] = data['game_icon']
            yield item
