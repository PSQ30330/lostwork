from django.conf.urls import url

from project import views

urlpatterns =[
    url(r'^add_projet/$',views.add_project,name="添加实训题目"),
    url(r'^info/$',views.info,name="学生选题"),
    url(r'^select/$',views.select_project,name="houduan"),
    url(r'^xuanti/$',views.student_xunti,name ="选题")
]