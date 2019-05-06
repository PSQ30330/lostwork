import json
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from sgin.models import Chankan
from student.models import Student
from weekly import forms, models


# 学生录入周报
def add_weekly(request):
    if request.session.get('is_login', None):
        if request.method == "POST":
            weekly_form = forms.StudentWeeklyForm(request.POST)

            if weekly_form.is_valid():
                username = request.session.get('username')
                neirong = Student.objects.filter(username=username).all().first()
                stu_name = neirong.stu_name
                title = weekly_form.cleaned_data['title']
                plan_finish = weekly_form.cleaned_data['plan_finish']
                finished = weekly_form.cleaned_data['finished']
                content = weekly_form.cleaned_data['content']
                c_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

                new_pro = models.Weekly()
                new_pro.stu_username = username
                new_pro.stu_name = stu_name
                new_pro.title = title
                new_pro.plan_finish = plan_finish
                new_pro.finished = finished
                new_pro.content = content
                new_pro.c_time = c_time
                new_pro.save()

                return render(request,'weekly/add_successful.html/')

    weekly_form = forms.StudentWeeklyForm()

    return render(request, 'weekly/add_weekly.html', locals())

def teacher_input(request):
    if request.method=="POST":

        tea_chakanform =forms.TeacherInputForm(request.POST)
        if tea_chakanform.is_valid():
            username = tea_chakanform.cleaned_data['username']
            people = Chankan()
            people.username = username
            people.save()
            return render(request, 'weekly/teacher_chakan.html')


    tea_chakanform = forms.TeacherInputForm
    return render(request, 'weekly/teacher_input.html', locals())


def teacher_select(request):
        chakan = Chankan.objects.filter().first()
        user_list =[]
        username = chakan.username
        req = models.Weekly.objects.filter(stu_username=username).all()

        for item in req:
            user_info = {
                "username":item.stu_username,
                "stu_name":item.stu_name,
                "title":item.title,
                "plan_finish":item.plan_finish,
                "finished":item.finished,
                "content":item.content,
                "c_time":item.c_time,
            }
            user_list.append(user_info)
        user_dic = {}
        user_dic['data'] = user_list
        Chankan.objects.filter(username=username).delete()
        return HttpResponse(json.dumps(user_dic))