# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from mysite import models, forms
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
        try:
            user = User.objects.get(username=username)
            diaries = models.Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass
    messages.get_messages(request)
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)


@login_required(login_url='/login/')
def contact(request):
    if request.user.is_authenticated():
        username = request.user.username
    messages.get_messages(request)
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


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(
                        request, messages.SUCCESS, 'You are logged in.')
                    return redirect('/')
                else:
                    messages.add_message(
                        request, messages.WARNING, "You have not registe.")
            else:
                messages.add_message(
                    request, messages.WARNING, 'There have some situation, can\'t find the user.')
        else:
            messages.add_message(request, messages.INFO,
                                 'Please checking the inputing fields. ')
    else:
        login_form = forms.LoginForm()
    template = get_template("login.html")
    html = template.render(context=locals(), request=request)
    response = HttpResponse(html)
    return response


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, 'You are logout. ')
    return redirect("/")


@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated():
        username = request.user.username
        try:
            user = User.objects.get(username=username)
            userinfo = models.Profile.objects.get(user=user)
        except:
            pass
    template = get_template('userinfo.html')
    html = template.render(locals())
    return HttpResponse(html)


@login_required(login_url='/login/')
def posting(request):
    if request.user.is_authenticated():
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    if request.method == 'POST':
        user = User.objects.get(username=username)
        diary = models.Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO,
                                 'message was stored. ')
            post_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.add_message(
                request, messages.INFO, 'if you want to post a message, you should fill all the blanks. ')
    else:
        post_form = forms.DiaryForm()
        messages.add_message(
            request, messages.INFO, 'if you want to post a message, you should fill all the blanks. ')
    template = get_template('posting.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)
