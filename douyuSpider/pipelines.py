# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from douyuSpider.sqlhelper import MysqlHelper
from douyuSpider.items import DouyuspiderItem

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

        if item.__class__ == DouyuspiderItem:
            params = [item['cate_id'],item['game_name'],item['short_name'],item['game_url'],item['game_src'],item['game_icon']]
            sql = 'insert into all_game(cate_id,game_name,short_name,game_url,game_src,game_icon) values(%s,' \
                  '%s,%s,%s,%s,%s);'

            self.mysqlhelper.insert(sql,params)
            return item

''''
try:
                self.cursor.execute("""select * from video_review_douban where review_url = %s""", item["review_url"])
                ret = self.cursor.fetchone()
                if ret:
                    self.cursor.execute(
                        """update video_review_douban set review_title = %s,review_content = %s,review_author = %s,
                            review_video = %s,review_time = %s,review_url = %s
                            where review_url = %s""",
                        (item['review_title'],
                         item['review_content'],
                         item['review_author'],
                         item['review_video'],
                         item['review_time'],
                         item['review_url'],
                         item['review_url']))
                else:
                    self.cursor.execute(
                        """insert into video_review_douban(review_title,review_content,review_author,review_video,review_time,
                          review_url)
                          value (%s,%s,%s,%s,%s,%s)""",
                        (item['review_title'],
                         item['review_content'],
                         item['review_author'],
                         item['review_video'],
                         item['review_time'],
                         item['review_url']))
                self.connect.commit()
            except Exception as error:
                log(error)
            return item
        else:
            pass
'''