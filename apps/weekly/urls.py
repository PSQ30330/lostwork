from django.conf.urls import url

from weekly import views

urlpatterns = [
    url(r'^add_weekly/$',views.add_weekly,name='周报'),
    url(r'^teacher_input/$',views.teacher_input,name='查询周报'),
    url(r'^teacher_chakan/$',views.teacher_select,name='显示周报'),
]