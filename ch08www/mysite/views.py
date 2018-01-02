# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from mysite import models, forms


# Create your views here.


def index(request, pid=None, del_pass=None):
    template = get_template('index.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = 'you should finish all the blank if you want to post a message...'
    if del_pass and pid:
        try:
            post = models.Post.objects.get(id=pid)
        except:
            post = None
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "data was removed successfully!"
            else:
                message = "your password was wrong!"
    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(
            mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = 'storage successively! Please remember your password [{}]!, message will be show after the check.'.format(
            user_pass)

    html = template.render(locals())
    return HttpResponse(html)


def listing(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(
        enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)


def posting(request):
    template = get_template('posting.html')
    moods = models.Mood.objects.all()
    message = 'you should fill all the blanks as you want to posting a message...'
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


def posting2(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = 'your messages would not be seen until admin\'s checking...'
            post_form.save()
            return HttpResponseRedirect('/list/')
        else:
            message = 'If you want to post a message, you have to fill all the blanks...'
    else:
        post_form = forms.PostForm()
        message = 'If you want to post a message, you have to fill all the blanks...'
    template = get_template('posting2.html')
    moods = models.Mood.objects.all()
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "Thank you for your letter!"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
        else:
            message = "Please check the information, is it correct?"
    else:
        form = forms.ContactForm()
    template = get_template('contact.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)
