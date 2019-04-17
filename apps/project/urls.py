from django.conf.urls import url

from project import views

urlpatterns =[
    url(r'^add_projet/$',views.add_project,name="添加实训题目")
]