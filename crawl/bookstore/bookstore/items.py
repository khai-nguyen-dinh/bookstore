# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BookstoreItem(scrapy.Item):
    book_name = scrapy.Field()
    price = scrapy.Field()
    thumbnail = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()
