from django.db import models

# Create your models here.
from student.models import Student


class TeacherProject(models.Model):

    gender = (
        ('1', "校内"),
        ('2', "校外"),
    )

    pro_id = models.AutoField(max_length=11,primary_key=True,verbose_name="编号")
    pro_title = models.CharField(max_length=40,verbose_name="标题")
    pro_type = models.CharField(max_length=32,choices=gender,default='校内',verbose_name='课题类型')
    pro_teacher = models.CharField(max_length=15,verbose_name='指导老师')
    pro_content = models.TextField(max_length=1000,verbose_name='课题内容')
    pro_count = models.IntegerField(verbose_name="学生选题人数")
    c_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    has_confirmed = models.BooleanField(default=False,verbose_name="管理员审核状态")

    def __str__(self):
        return self.pro_title

    class Meta:
        db_table = 'project'
        ordering = ['-c_time']
        verbose_name = "实训题目"
        verbose_name_plural = "实训题目"

# class StudentSelect(models.Model):
#     stu_username = models.ForeignKey(Student)
#     stu_proid = models.ForeignKey(TeacherProject)
#     c_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#
#     def __str__(self):
#         return self.stu_username
#
#     class Meta:
#         db_table = 'student_select'
#         ordering = ['-c_time']
#         verbose_name = "学生选题"
#         verbose_name_plural = "学生选题"
#
#
#
# class StudentSelectNum(models.Model):
#
#     stu_num = models.IntegerField(null=True,verbose_name="学生人数")
#     stu_selectnum = models.IntegerField(null=True,verbose_name="选题人数")
#     stu_noselectnum = models.IntegerField(null=True,validators="未选人数")
#
#     def __str__(self):
#         return self.stu_num,self.stu_selectnum,self.stu_noselectnum
#
#     class Meta:
#         db_table = 'student_select_num'
#         ordering = ['-c_time']
#         verbose_name = "学生选题"
#         verbose_name_plural = "学生选题"