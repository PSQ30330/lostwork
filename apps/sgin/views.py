# Create your views here.
import json
import time

from django.http import HttpResponse
from django.shortcuts import redirect, render

from sgin import forms, models
from student.models import Student

# 学生签到
def student_sgin(request):
    if request.session.get('is_login', None):

        if request.method == "POST":
            num = request.session.get('username')
            sgin_form=forms.StudentSginForm(request.POST)

            if sgin_form.is_valid():
                username = sgin_form.cleaned_data['username']
                count = Student.objects.filter(username=username).all().first()
                time_now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
                beizhu = time.strftime("%Y-%m-%d",time.localtime(time.time()))

                duibi = models.Sgin.objects.filter(username=num).all().first()
                dui_bi = models.Sgin.objects.filter(username=num).count()
                if dui_bi == 0:
                    student_name = count.stu_name
                    new_user = models.Sgin()
                    new_user.username = username
                    new_user.stu_name = student_name
                    new_user.c_time = time_now
                    new_user.beizhu = beizhu
                    new_user.save()

                    return redirect('/student/index/')

                elif beizhu != duibi.beizhu:

                    student_name=count.stu_name
                    new_user = models.Sgin()
                    new_user.username=username
                    new_user.stu_name=student_name
                    new_user.c_time = time_now
                    new_user.beizhu = beizhu
                    new_user.save()

                    return redirect('/student/index/')
                else:
                    message = "今日已签到，无需再签到"
                    return render(request, 'sgin/student_sgin.html', locals())


    sgin_form = forms.StudentSginForm
    return render(request,'sgin/student_sgin.html',locals())

#学生查看签到数据
def chakan(request):
    return render(request,'sgin/student_chakan.html')

def student_chakan(requset):
    users_list = []
    username = requset.session.get('username')
    req = models.Sgin.objects.filter(username=username).all()

    for item in req:
        user_info = {
            "username":item.username,
            "stu_name":item.stu_name,
            "c_time":item.c_time,

        }
        users_list.append(user_info)

    user_dic = {}
    user_dic['data'] = users_list

    return HttpResponse(json.dumps(user_dic))

def teacher_input(request):
    if request.method=="POST":

        tea_chakanform =forms.StudentSginForm(request.POST)
        if tea_chakanform.is_valid():
            username = tea_chakanform.cleaned_data['username']
            people = models.Chankan()
            people.username = username
            people.save()
            return render(request,'sgin/teacher_chakan.html')


    tea_chakanform = forms.StudentSginForm
    return render(request, 'sgin/teacher_select.html', locals())


def teacher_select(request):
        chakan = models.Chankan.objects.filter().first()
        user_list =[]
        username = chakan.username
        req = models.Sgin.objects.filter(username=username).all()

        for item in req:
            user_info = {
                "username":item.username,
                "stu_name":item.stu_name,
                "c_time":item.c_time,
            }
            user_list.append(user_info)
        user_dic = {}
        user_dic['data'] = user_list
        models.Chankan.objects.filter(username=username).delete()
        return HttpResponse(json.dumps(user_dic))
