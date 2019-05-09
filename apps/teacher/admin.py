from django.contrib import admin

# Register your models here.
from project.models import Select_Over, Select_notok
from teacher.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username','tea_name','sex','emali','c_time','has_confirmed')
    list_display_links = ('username', 'tea_name')

class SelectOverAdmin(admin.ModelAdmin):
    list_display = ('xuan_username','xuan_stu_name','xuan_pro_title')

class SelectnotokAdmin(admin.ModelAdmin):
    list_display = ('notok_username','notok_stu_name','notok_pro_title')

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Select_Over,SelectOverAdmin)
admin.site.register(Select_notok,SelectnotokAdmin)
