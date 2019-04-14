
from django.db import models
class Teacher(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    username = models.CharField(max_length=15,unique=True, verbose_name='工号', primary_key=True)
    tea_name = models.CharField(max_length=32, verbose_name='姓名')
    password = models.CharField(max_length=128, validators='密码')
    sex = models.CharField(max_length=32, choices=gender, default="男", verbose_name='性别')
    emali = models.EmailField(unique=True,  verbose_name='电子邮件')
    c_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    has_confirmed = models.BooleanField(default=False,verbose_name="激活状态")
    class Meta:
        db_table = 'teacher'
        ordering = ['-c_time']
        verbose_name = '老师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    teacher = models.OneToOneField('Teacher')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacher.username + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"