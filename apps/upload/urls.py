from django.conf.urls import url

from upload import views

urlpatterns =[

url(r'^disk/$',views.register,name="上传"),
]