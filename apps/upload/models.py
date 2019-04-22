from django.db import models

# Create your models here.
class Files(models.Model):
    title = models.CharField(verbose_name='文件名',max_length=100,blank=True,default='')
    headfiles = models.FileField(verbose_name="文件路径",upload_to="./files/",blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'files_upload'
        ordering = ['date']
        verbose_name = "文件上传"
        verbose_name_plural = "文件上传"