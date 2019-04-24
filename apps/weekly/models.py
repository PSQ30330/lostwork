from django.db import models

# Create your models here.

class Weekly(models.Model):
    stu_username = models.CharField(max_length=15, verbose_name="学号")
    stu_name = models.CharField(max_length=15, null=True, verbose_name="姓名")
    title = models.CharField(max_length=15,  verbose_name="标题")
    plan_finish = models.TextField(max_length=5000, null=True, verbose_name="计划完成")
    finished = models.TextField(max_length=5000, null=True, verbose_name="实际完成")
    content = models.TextField(max_length=5000, null=True, verbose_name='问题与计划')
    c_time = models.CharField(max_length=32,null=True, verbose_name="选题时间")

    def __str__(self):
        return self.stu_username

    class Meta:
        db_table = 'student_weekly'
        ordering = ['-c_time']
        verbose_name = "学生周报"
        verbose_name_plural = "学生周报"