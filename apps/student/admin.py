from django.contrib import admin

# Register your models here.
from student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('username','stu_name','sex','emali','major','stu_class','c_time','has_confirmed')
    list_display_links =('username','stu_name')

admin.site.register(Student,StudentAdmin)