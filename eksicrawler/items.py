# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from applications.eksicrawler.models import EksiModel


class EksiItem(DjangoItem):
    django_model = EksiModel
