"""lostwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from student.views import index_view

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^student/', include('student.urls', namespace='student')),
    url(r'^teacher/', include('teacher.urls', namespace='teacher')),
    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^sgin/',include('sgin.urls',namespace='sgin')),
    url(r'^captcha', include('captcha.urls')),
    url(r'^upload/',include('upload.urls')),
    url(r'^weekly/',include('weekly.urls')),
    url(r'^comment/',include('comment.urls',namespace='comment')),
    url('^$',index_view)



]
