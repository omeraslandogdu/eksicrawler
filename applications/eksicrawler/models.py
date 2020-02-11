# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from applications.core.models import BaseModel
from django.db import models


class EksiModel(BaseModel):
    author = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
