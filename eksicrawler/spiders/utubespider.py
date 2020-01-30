# -*- coding: utf-8 -*-
import scrapy


class UtubespiderSpider(scrapy.Spider):
    name = 'utubespider'
    allowed_domains = ['https://eksisozluk.com/takip-edilesi-youtube-kanallari--2929069']
    start_urls = ['http://https://eksisozluk.com/takip-edilesi-youtube-kanallari--2929069/']

    def parse(self, response):
        pass
