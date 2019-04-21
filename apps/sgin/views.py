# Create your views here.
import time

from django.shortcuts import redirect, render

from sgin import forms, models
from student.models import Student


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
    return  render(request,'sgin/student_sgin.html',locals())