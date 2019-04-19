import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from project import forms, models
from project.models import StudentSelect, TeacherProject


def add_project(request):

    if request.session.get('is_login', None):
        if request.method == "POST":
            add_form = forms.ProForm(request.POST)

            if add_form.is_valid():

                pro_title = add_form.cleaned_data['pro_title']
                pro_type = add_form.cleaned_data['pro_type']
                pro_teacher = add_form.cleaned_data['pro_teacher']
                pro_content = add_form.cleaned_data['pro_content']
                pro_count = add_form.cleaned_data['pro_count']

                same_pro_title = models.TeacherProject.objects.filter(pro_title=pro_title)

                if same_pro_title:
                    message = "该题目已经录入，无需重复录入"

                    return render(request,'project/add_projet.html',locals())
                else:
                    new_pro = models.TeacherProject()
                    new_pro.pro_title = pro_title
                    new_pro.pro_type = pro_type
                    new_pro.pro_teacher = pro_teacher
                    new_pro.pro_content = pro_content
                    new_pro.pro_count = pro_count

                    new_pro.save()

                    return redirect('/teacher/index/')


    add_form = forms.ProForm()

    return render(request,'project/add_projet.html',locals())


def info(requset):
    return render(requset,'project/student_select.html')

def select_project(request):

    users_list = []
    req =TeacherProject.objects.all()


    for item in req:
        user_info= {
        "pro_id":item.pro_id,
        "pro_title":item.pro_title,
        "pro_type":item.pro_type,
        "pro_teacher":item.pro_teacher,
        "pro_content":item.pro_content,
        "pro_count":item.pro_count,
        "bei_zhu":item.bei_zhu,
        "fa_za":item.fa_za,
        "fei_gong":item.fei_gong,

        }
        users_list.append(user_info)
    user_dic = {}

    user_dic['data'] = users_list
    return HttpResponse(json.dumps(user_dic))






