# -*- coding: utf-8 -*-
from django import forms
from mysite import models
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(label='name', max_length='20')
    password = forms.CharField(label='password', widget=forms.PasswordInput())


class DateInput(forms.DateInput):
    input_type = 'date'


class DiaryForm(forms.ModelForm):
    class Meta:
        model = models.Diary
        fields = ['budget', 'weight', 'note', 'ddate']
        widgets = {'ddate': DateInput(), }

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = '今日花费（元）'
        self.fields['weight'].label = '今日体重（ＫＧ）'
        self.fields['note'].label = '心情留言'
        self.fields['ddate'].label = '日期'


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
