from django.conf.urls import url

from sgin import views

urlpatterns =[
    url(r'^sgin/$',views.student_sgin,name='签到'),
    url(r'^chakan/$',views.chakan,name="学生查看考勤"),
    url(r'^stu_chakan/$',views.student_chakan),
    url(r'^tea_select/$',views.teacher_input),
    url(r'^tea_chakan/$',views.teacher_select),
]