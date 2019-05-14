from django.db import models

# Create your models here.
class Comment(models.Model):
    pro_id = models.CharField(max_length=11,verbose_name='文章标题编号')
    parent_id = models.CharField(max_length=11,null=True,verbose_name='评论编号')
    username = models.CharField(max_length=15,verbose_name='用户编号')
    content = models.TextField(max_length=300,verbose_name='评论')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")


    def __str__(self):
        return self.pro_id

    class Meta:
        db_table = 'project_comment'

        verbose_name = "讨论/提问"
        verbose_name_plural = "讨论/提问"

