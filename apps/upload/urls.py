from django.conf.urls import url

from upload import views

urlpatterns =[

    url(r'^disk/$',views.register,name="upload"),
    url(r'^tea_select/$', views.teacher_input),
    url(r'^tea_chakan/$', views.teacher_select),

    url(r'^home/$', views.render_home_template, name='home'),

    url(r'^download/(?P<filename>.+)$', views.download, name='download'),
    ]