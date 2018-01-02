# -*- coding: utf-8 -*-
from django import forms
from mysite import models
from captcha.fields import CaptchaField


class PostForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_pass']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '现在的心情'
        self.fields['nickname'].label = '您的昵称'
        self.fields['message'].label = '心情留言'
        self.fields['del_pass'].label = '设置密码'
        self.fields['captcha'].label = '确定您不是机器人'


class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaosiung'],
        ['NA', 'Others'],
    ]
    user_name = forms.CharField(
        label='Your name', max_length=50, initial='DaRen Li')
    user_city = forms.ChoiceField(label='living city', choices=CITY)
    user_school = forms.BooleanField(label='in or not', required=False)
    user_email = forms.EmailField(label='Email')
    user_message = forms.CharField(label='your advice', widget=forms.Textarea)
