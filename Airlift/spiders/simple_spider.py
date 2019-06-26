# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:51:11 2019

@author: gakel
"""

from scrapy import Spider
from Airlift.item import AirliftItem

    name = 'simple_spider'
	allowed_urls = ['https://en.wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/List_of_military_transport_aircraft']