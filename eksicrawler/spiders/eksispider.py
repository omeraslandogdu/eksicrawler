# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from eksicrawler.items import EksiItem

class EskiSpider(scrapy.Spider):
    name = 'eksi'
    allowed_domains = ['eksisozluk.com']
    start_urls = ['https://eksisozluk.com/takip-edilesi-youtube-kanallari--2929069/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = EksiItem()
        select = response.xpath('//*[@id="entry-item-list"]')
        for sel in select.xpath('//li'):
            item['author'] = sel.xpath('//footer/div[2]/a[2]').extract_first()
            item['url'] = sel.xpath('//div[1]/a').extract_first()
            yield item
            yield Request(response.url, callback=self.parse)
