import json
import os
import time

from django import forms
from django.core.files import File
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET


from sgin.models import Chankan
from student.models import Student
from upload.models import Files


class UserForm(forms.Form):
    title = forms.CharField()
    headfiles = forms.FileField()


def register(request):
    if request.method == "POST":
        username =request.session.get('username')
        neirong = Student.objects.filter(username=username).all().first()
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            title = uf.cleaned_data['title']
            headfiles =uf.cleaned_data['headfiles']
            time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            user = Files()
            user.username = username
            user.stu_nema = neirong.stu_name
            user.title =title
            user.date = time_now
            user.headfiles = headfiles
            user.save()
            return render(request,'upload/upload_successful.html')
    else:
        uf = UserForm()
    return render(request, 'upload/register.html',locals())

def teacher_input(request):
    from sgin import models, forms
    if request.method=="POST":

        tea_chakanform =forms.StudentSginForm(request.POST)

        if tea_chakanform.is_valid():
            username = tea_chakanform.cleaned_data['username']
            people = models.Chankan()
            people.username = username
            people.save()
            return render(request,'upload/teacher_chakan.html')


    tea_chakanform = forms.StudentSginForm
    return render(request, 'upload/teacher_select.html', locals())


def teacher_select(request):
        chakan = Chankan.objects.filter().first()
        user_list =[]
        username = chakan.username
        req = Files.objects.filter(username=username).all()

        for item in req:
            user_info = {
                "username":item.username,
                "stu_name":item.stu_nema,
                'title':item.title,
                "headfiles":str(item.headfiles),
                "date":item.date,
            }
            user_list.append(user_info)
        user_dic = {}
        user_dic['data'] = user_list
        Chankan.objects.filter(username=username).delete()
        return HttpResponse(json.dumps(user_dic))


# 文件下载
SAVED_FILES_DIR = r'./media/files/'

def render_home_template(request):
    files = os.listdir(SAVED_FILES_DIR)
    return render(request, 'upload/home.html', {'files': files})

@require_GET
def download(request, filename):
    file_pathname = os.path.join(SAVED_FILES_DIR, filename)

    with open(file_pathname, 'rb') as f:
        file = File(f)

        response = HttpResponse(file.chunks(),
                                content_type='APPLICATION/OCTET-STREAM')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Length'] = os.path.getsize(file_pathname)

    return response