from django.shortcuts import render, redirect

# Create your views here.
from project import forms, models


def add_project(request):
    # if request.method == "GET":
    #     return render(request,'project/add_projet.html',locals())
    if request.session.get('is_login', None):
        if request.method == "POST":
            add_form = forms.ProForm(request.POST)
            print(add_form)
            if add_form.is_valid():

                pro_title = add_form.cleaned_data['pro_title']
                pro_type = add_form.cleaned_data['pro_type']
                pro_teacher = add_form.cleaned_data['pro_teacher']
                pro_content = add_form.cleaned_data['pro_content']
                pro_count = add_form.cleaned_data['pro_count']

                same_pro_title = models.TeacherProject.objects.filter(pro_title=pro_title)
                print('2')
                if same_pro_title:
                    message = "该题目已经录入，无需重复录入"
                    print('3')
                    return render(request,'project/add_projet.html',locals())
                else:
                    new_pro = models.TeacherProject()
                    new_pro.pro_title = pro_title
                    new_pro.pro_type = pro_type
                    new_pro.pro_teacher = pro_teacher
                    new_pro.pro_content = pro_content
                    new_pro.pro_count = pro_count

                    new_pro.save()
                    print('4')
                    return redirect('/teacher/index/')
    add_form = forms.ProForm()
    print('5')
    return render(request,'project/add_projet.html',locals())


