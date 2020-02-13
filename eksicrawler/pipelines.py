# -*- coding: utf-8 -*-

from applications.eksicrawler.models import EksiModel

class EksiPipeline(object):
    def process_item(self, item, spider):
        eksimodel = EksiModel()
        eksimodel.save(item)
        return item
