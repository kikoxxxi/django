# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Maker(models.Model):
    name=models.CharField(max_length=10)
    country=models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
class PModel(models.Model):
    maker=models.ForeignKey(Maker,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    url=models.URLField(default='https://note.youdao.com/yws/public/resource/08345447630fc566479d74186c0cf507/xmlnote/WEBRESOURCEa62cb32ae78504929bf5138b992c2f9c/2647')

    def __unicode__(self):
        return self.name
class Product(models.Model):
    pmodel=models.ForeignKey(PModel,on_delete=models.CASCADE,verbose_name='型号')
    nickname=models.CharField(max_length=15,default='超值二手手机',verbose_name='摘要')
    description=models.TextField(default='暂无说明')
    year=models.PositiveIntegerField(default=2016,verbose_name='出厂年份')
    price=models.PositiveIntegerField(default=0,verbose_name='价格')

    def __unicode__(self):
        return self.nickname
class PPhoto(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    description=models.CharField(max_length=20,default='产品照片')
    url=models.URLField(default='https://note.youdao.com/yws/public/resource/08345447630fc566479d74186c0cf507/xmlnote/WEBRESOURCEdbfaa126a02dfc98dc446e7718618051/2652')

    def __unicode__(self):
        return self.description
