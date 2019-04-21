from django.conf.urls import url

from sgin import views

urlpatterns =[
    url(r'^sgin/$',views.student_sgin,name='签到'),
]