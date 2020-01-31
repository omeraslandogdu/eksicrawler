# -*- coding: utf-8 -*-
import scrapy


class EskiSpider(scrapy.Spider):
    name = 'eksi'
    allowed_domains = ['https://eksisozluk.com/takip-edilesi-youtube-kanallari--2929069']
    start_urls = ['http://https://eksisozluk.com/takip-edilesi-youtube-kanallari--2929069/']

    def parse(self, response):
        pass
