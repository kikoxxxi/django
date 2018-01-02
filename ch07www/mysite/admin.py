# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('pmodel','nickname','price','year')
    search_fields=('nickname',)
    ordering=('-price',)
admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.PPhoto)
