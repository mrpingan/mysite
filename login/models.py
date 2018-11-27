from django.db import models

# Create your models here.

class User(models.Model):

    gender = (
        ('male','男'),
        ('female','女'),
        ('unknow','未知'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default="未知")
    create_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "user"
        ordering = ['-create_at']
        verbose_name = "用户"
        verbose_name_plural = "用户管理"

    def __str__(self):
        return self.name

