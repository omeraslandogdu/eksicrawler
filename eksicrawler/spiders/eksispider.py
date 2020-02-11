# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from eksicrawler.items import EksiItem

class EskiSpider(scrapy.Spider):
    name = 'eksi'
    allowed_domains = ['https://eksisozluk.com/']
    start_urls = ['https://eksisozluk.com/takip-edilesi-youtube-kanallari--2929069/']

    def parse(self, response):
        item = EksiItem()
        select = response.selector.css('#entry-item-list')
        for sel in select:
            item['author'] = sel.css('.footer > div.info > a.entry-author').extract_first()
            item['url'] = sel.css('.project-title-text > a ::attr(href)').extract_first()
            print(item)
            yield Request(response.url, callback=self.parse)
