from django.contrib import admin

# Register your models here.
from project.models import TeacherProject


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pro_id','pro_title','pro_type','pro_content','pro_count','c_time','bei_zhu','fa_za','fei_gong','has_confirmed')

    list_display_links = ('pro_id','pro_title')

admin.site.register(TeacherProject,ProjectAdmin)

