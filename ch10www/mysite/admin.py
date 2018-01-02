# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite import models

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'enabled')
    ordering = ('-name',)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile)
admin.site.register(models.Diary)
