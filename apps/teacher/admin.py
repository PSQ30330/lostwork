from django.contrib import admin

# Register your models here.
from teacher.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username','tea_name','sex','emali','c_time','has_confirmed')


admin.site.register(Teacher,TeacherAdmin)