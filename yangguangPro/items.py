# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangproItem(scrapy.Item):
    # define the fields for your item here like:
    id_num = scrapy.Field()
    title = scrapy.Field()
class YangguangproTail(scrapy.Item):
    num_id = scrapy.Field()
    content = scrapy.Field()
