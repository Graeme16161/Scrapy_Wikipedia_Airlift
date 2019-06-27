# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:51:11 2019

@author: gakel
"""

from scrapy import Spider
from Airlift.items import AirliftItem

class AirliftSpider(Spider):
    
    name = 'simple_spider'
    allowed_urls = ['https://en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_military_transport_aircraft']
    
    def parse(self, response):
        rows = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr')
        
        
        for row in rows:
            
            model = row.xpath('./td[1]/a/text()').extract_first()
            
            #//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td[2]
            country = row.xpath('./td[2]/text()').extract_first()
            
            #//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td[3]
            aircraft_class = row.xpath('./td[3]/text()').extract_first()
            
            #//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td[5]
            date = row.xpath('./td[5]/text()').extract_first()
            
            #//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td[6]
            payload_t = row.xpath('./td[6]/text()').extract_first()
            
            #//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td[7]
            range_km = row.xpath('./td[7]/text()').extract_first()
            
            item = AirliftItem()
            item['model'] = model
            item['country'] = country
            item['aircraft_class'] = aircraft_class
            item['date'] = date
            item['payload_t'] = payload_t
            item['range_km'] = range_km
            yield item
        
    
    