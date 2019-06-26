# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirliftItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model = scrapy.Field()
    country = scrapy.Field()
    aircraft_class = scrapy.Field()
    date = scrapy.Field()
    payload_t = scrapy.Field()
    range_km = scrapy.Field()
    
