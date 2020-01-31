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
        for sel in select.css('li:nth-child(2)'):
            item['no'] = sel.css('::attr(data-id)').extract_first()
            item['url'] = sel.css('.project-title-text > a ::attr(href)').extract_first()
            item['price'] = sel.css('.price ::text').extract_first()
            item['title'] = sel.css('.project-title-text a span ::text').extract_first()
            item['district'] = sel.css('.location-info span.location-name ::text').extract_first()
            item['featured'] = sel.css('.listing-energy').extract_first()
            item['location'] = sel.css('.location-info span.location-name ::text').extract_first()
            item['info_data'] = sel.css('div.span ::text').extract_first()
            item['listing_date'] = sel.css('.due-date ::text').extract_first()
            item['square_meter'] = sel.css('.size-summary strong ::text').extract_first()
            item['listing_count'] = sel.css('strong.result-number ::text').extract_first()
            item['property_type'] = sel.css('span.listing-property-type-name ::text').extract_first()
            item['number_of_rooms'] = sel.css('.room-count ::text').extract_first()
            yield item
            yield Request(response.url, callback=self.parse)
