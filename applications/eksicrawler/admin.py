# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import EksiModel

# Register your models here.


@admin.register(EksiModel)
class EksiAdmin(ModelAdmin):
    list_display = (
        'id',
        'author',
        'url',
        'created_at',
        'updated_at',
        'status',
    )