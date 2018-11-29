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

class RegisterForm(forms.Form):
    sex = {
        ('M',"男"),
        ('F',"女"),
        ('N',"未知"),
    }

    username = forms.CharField(label="用户名",max_length=128,
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="密码",max_length=256,
                                widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="确认密码",max_length=256,
                                widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="邮箱地址",widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex = forms.ChoiceField(label="性别",choices=sex)
    captcha = CaptchaField(label="验证码")