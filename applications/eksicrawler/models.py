# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from applications.core.models import BaseModel
from django.db import models


class EksiModel(BaseModel):
    author = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def eksi_save(self, data):
        try:
            eksimodel = EksiModel.create(
                url=str(data['url']),
                price=str(data['price']),
                author=str(data['author']),
                status=BaseModel.STATUS_ACTIVE
            )
            return dict(eksimodel)
        except:
            pass