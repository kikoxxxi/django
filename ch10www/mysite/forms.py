# -*- coding: utf-8 -*-
from django import forms
from mysite import models
from django.contrib.auth.models import User
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


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Password'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '昵称'
        self.fields['password'].label = '密码'
        self.fields['email'].label = '邮箱'
        self.fields['first_name'].label = '姓'
        self.fields['last_name'].label = '名'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['height', 'male', 'website']
        widgets = {'height': forms.TextInput(attrs={'class': 'form-control'}),
                   'website': forms.TextInput(attrs={'class': 'form-control'}), }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['height'].label = '身高（cm）'
        self.fields['male'].label = '是男生吗'
        self.fields['website'].label = '个人网站'


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
