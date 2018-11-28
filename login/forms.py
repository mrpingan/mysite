#!/usr/bin/env python
#coding:utf-8
__author__ = 'ping'
__time__ = '2018/11/28 18:59'

from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=128,required=True)
    password = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput)
