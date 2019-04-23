from django.db import models

# Create your models here.
class Files(models.Model):
    username = models.CharField(max_length=15,null=True,verbose_name='上传者')
    stu_nema = models.CharField(max_length=32,null=True,verbose_name='上传者姓名')
    title = models.CharField(verbose_name='标题',max_length=100,blank=True,default='')
    headfiles = models.FileField(verbose_name="文件路径",upload_to="./files/",blank=True)
    date = models.CharField(max_length=100, verbose_name="上传时间")

    def __unicode__(self):
        return self.title,self.username

    def __str__(self):
        return self.title,self.username

    class Meta:
        db_table = 'files_upload'
        ordering = ['date']
        verbose_name = "文件上传"
        verbose_name_plural = "文件上传"