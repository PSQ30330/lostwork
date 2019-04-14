from django.contrib import admin

# Register your models here.
from student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('username','stu_name','sex','emali','major','stu_class','c_time','has_confirmed')
admin.site.register(Student,StudentAdmin)