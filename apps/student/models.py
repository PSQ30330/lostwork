

# Create your models here.
from django.db import models


class Student(models.Model):
    """
        学生模型
    """

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    username = models.CharField(max_length=15,unique=True,verbose_name='学号',primary_key=True)
    stu_name = models.CharField(max_length=32,verbose_name='姓名')
    password = models.CharField(max_length=128,validators='密码')
    sex = models.CharField(max_length=32, choices=gender, default="男",verbose_name='性别')
    emali = models.EmailField(unique=True,verbose_name='电子邮件')
    major = models.CharField(max_length=15,verbose_name='专业')
    stu_class = models.CharField(max_length=15,verbose_name='班级')
    c_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    has_confirmed = models.BooleanField(default=False)


    class Meta:
        db_table = 'student'
        ordering = ['-c_time']
        verbose_name = '学生'
        verbose_name_plural = verbose_name

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    student = models.OneToOneField('Student')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"



