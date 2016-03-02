# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field 
class ZhiboItem(Item):
    title = Field()
    link = Field()
    zhubo = Field()
    view = Field()
    img_url = Field()
    image_urls = Field()
    images = Field()
    web = Field()
    cate = Field()
    active = Field()

