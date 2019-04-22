from django.db import models

# Create your models here.
class Sgin(models.Model):
    username = models.CharField(max_length=15,null=True,verbose_name="学号")
    stu_name = models.CharField(max_length=32,null=True,verbose_name="姓名")
    c_time = models.CharField(max_length=100,null=True,verbose_name="签到时间")
    beizhu = models.CharField(max_length=100,null=True,verbose_name='备注')


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'student_sgin'
        ordering = ['-c_time']
        verbose_name = "学生签到"
        verbose_name_plural = "学生签到"

class Chankan(models.Model):
    username = models.CharField(max_length=15,null=True,verbose_name="学号")

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'teacher_chakan'
        verbose_name = "老师查看学生签到"
        verbose_name_plural = "老师查看学生签到"