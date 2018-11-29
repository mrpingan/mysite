#!/usr/bin/env python
#coding:utf-8
__author__ = 'ping'
__time__ = '2018/11/29 16:23'

import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        subject='来自Django的测试邮件',
        message='This is a test!',
        from_email='qq.ping@ybm100.com',
        recipient_list=['921194882@qq.com'],
    )