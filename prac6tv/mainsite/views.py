# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request,tvno='0'):
    tv_list=[{'name':'oneday正片','tvcode':'XNjkxNzM2NzAw'},
        {'name':'oneday预告','tvcode':'XMjYzMDU0NjQw'},]
    template=get_template('index.html')
    now=datetime.now()
    hour=now.timetuple().tm_hour
    tvno=tvno
    tv=tv_list[int(tvno)]
    html=template.render(locals())
    return HttpResponse(html)
