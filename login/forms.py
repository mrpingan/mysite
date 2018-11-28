#!/usr/bin/env python
#coding:utf-8
__author__ = 'ping'
__time__ = '2018/11/28 18:59'

from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=128,required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    password = forms.CharField(label="密码",max_length=256,
                               widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    captcha = CaptchaField(label="验证码")