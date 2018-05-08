# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cate_id = scrapy.Field()
    game_name = scrapy.Field()
    short_name = scrapy.Field()
    game_url = scrapy.Field()
    game_src = scrapy.Field()
    game_icon = scrapy.Field()

class DouyuRoomItem(scrapy.Item):

    room_id = scrapy.Field()
    ower_uid = scrapy.Field()
    nickname = scrapy.Field()
    url = scrapy.Field()
