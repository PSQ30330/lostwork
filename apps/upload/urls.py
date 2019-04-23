from django.conf.urls import url

from upload import views

urlpatterns =[

    url(r'^disk/$',views.register,name="上传"),
    url(r'^tea_select/$', views.teacher_input),
    url(r'^tea_chakan/$', views.teacher_select),
    ]