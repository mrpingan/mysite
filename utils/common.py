#!/usr/bin/env python
#coding:utf-8
__author__ = 'ping'
__time__ = '2018/11/29 17:11'

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import datetime
from login import models
import hashlib

def send_email(email, code):

    subject = "来自Django的注册确认邮件"
    text_content = """
        感谢注册www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！\
如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！
    """
    html_content = """
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.liujiangblog.com</a>，\
                    这里是刘江的博客和教程站点，专注于Python和Django技术的分享！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
    """.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name,now)
    models.ConfirmString.objects.create(code=code,user=user,)
    return code

def hash_code(s,salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()