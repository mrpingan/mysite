from django.db import models

# Create your models here.

class User(models.Model):

    gender = (
        ('M','男'),
        ('F','女'),
        ('N','未知'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default="未知")
    create_at = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)


    class Meta:
        db_table = "user"
        ordering = ['-create_at']
        verbose_name = "用户"
        verbose_name_plural = "用户管理"

    def __str__(self):
        return self.name


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User')
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tb_confirm"
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"

    def __str__(self):
        return self.user.name + ":" + self.code
