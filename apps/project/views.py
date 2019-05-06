import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from project import forms, models
from project.forms import KaoHeForm
from project.models import Select_Over, Select_notok
from project.models import TeacherProject

# 老师录入课题
from student.models import Student


def add_project(request):

    if request.method == "POST":
        username = request.session.get('username')
        # neirong  = Teacher.objects.filter(username=username).all().first()
        tea_name = request.session.get('tea_name')
        add_form = forms.ProForm(request.POST)


        if add_form.is_valid():
            pro_title = add_form.cleaned_data['pro_title']
            pro_type = add_form.cleaned_data['pro_type']
            pro_teacher = tea_name
            pro_content = add_form.cleaned_data['pro_content']
            pro_count = add_form.cleaned_data['pro_count']
            same_pro_title = models.TeacherProject.objects.filter(pro_title=pro_title)

            if same_pro_title:
                message = "该题目已经录入，无需重复录入"

                return render(request, 'project/add_projet.html', locals())
            else:
                new_pro = models.TeacherProject()
                new_pro.pro_title = pro_title
                new_pro.pro_type = pro_type
                new_pro.pro_username= username
                new_pro.pro_teacher = pro_teacher
                new_pro.pro_content = pro_content
                new_pro.pro_count = pro_count

                new_pro.save()

                return render(request,'project/pro_successful.html')

    add_form = forms.ProForm()

    return render(request, 'project/add_projet.html', locals())





# 学生查看可选的课题
def info(requset):
    return render(requset, 'project/student_select.html')


def select_project(request):
    users_list = []
    req = TeacherProject.objects.all()

    for item in req:
        if item.has_confirmed == True:
            user_info = {
                "pro_id": item.pro_id,
                "pro_title": item.pro_title,
                "pro_type": item.pro_type,
                "pro_teacher": item.pro_teacher,
                "pro_content": item.pro_content,
                "pro_count": item.pro_count,
                "bei_zhu": item.bei_zhu,
                "fa_za": item.fa_za,
                "fei_gong": item.fei_gong,

            }
            users_list.append(user_info)
    user_dic = {}

    user_dic['data'] = users_list
    return HttpResponse(json.dumps(user_dic))

# 学生选题
def student_xunti(requset):
    if requset.method == 'POST':
        username = requset.session.get('username')
        stu_name = requset.session.get('stu_name')
        stu_xunti_form = forms.XuanTiForm(requset.POST)
        if stu_xunti_form.is_valid():
            pro_id = stu_xunti_form.cleaned_data['stu_proid']
            id = models.StudentSelect.objects.filter(stu_username =username ).count()
            if id > 0:
                message = "已经选过实训题目，无需再添加"
                return render(requset, 'project/student_xuanti.html', locals())
            else:
                neirong = models.TeacherProject.objects.filter(pro_id=pro_id).all().first()
                stu_username = username
                pro_title = neirong.pro_title
                pro_type = neirong.pro_type
                pro_teacher = neirong.pro_teacher
                pro_content = neirong.pro_content
                pro_count = neirong.pro_count
                fei_gong = neirong.fei_gong

                new_user = models.StudentSelect()
                new_user.stu_username = stu_username
                new_user.stu_name = stu_name
                new_user.stu_proid = pro_id
                new_user.pro_title = pro_title
                new_user.pro_type = pro_type
                new_user.pro_teacher = pro_teacher
                new_user.pro_content = pro_content
                new_user.pro_count = pro_count
                new_user.fei_gong = fei_gong

                new_user.save()
                models.TeacherProject.objects.filter(pro_id=pro_id).delete()
                return render(requset,'project/select_successful.html/')

    stu_xunti_form = forms.XuanTiForm
    return render(requset, 'project/student_xuanti.html', locals())

# 学生查看自己选择的课题
def chakan(request):
    return render(request, 'project/chakan.html')


def stu_chakan(requset):
    users_list = []
    username = requset.session.get('username')

    req = models.StudentSelect.objects.filter(stu_username=username).all()

    for item in req:
        user_info = {
            "stu_username": item.stu_username,
            'stu_name':item.stu_name,
            "stu_proid": item.stu_proid,
            "pro_title": item.pro_title,
            "pro_type": item.pro_type,
            "pro_teacher": item.pro_teacher,
            "pro_content": item.pro_content,
            "pro_count": item.pro_count,
            "fei_gong": item.fei_gong,

        }
        users_list.append(user_info)
    user_dic = {}

    user_dic['data'] = users_list
    return HttpResponse(json.dumps(user_dic))

# 学生选题情况表
def select_situation(request):


    new_user =models.Student.objects.all()
    newok_user = models.StudentSelect.objects.all()

    for i in new_user:
        ok_user = models.Select_Over.objects.filter(xuan_username=i.username)

        not_ok = models.Select_notok()
        new = models.Select_notok.objects.filter(notok_username=i.username)


        if (new.count() == 0) and (ok_user.count() ==0) :

            not_ok.notok_username = i.username

            not_ok.notok_stu_name = i.stu_name


            not_ok.save()


    for user in newok_user:
        user_ok = models.Select_Over()
        oku = models.Select_Over.objects.filter(xuan_username=user.stu_username)


        if oku.count() == 0:
            user_ok.xuan_username = user.stu_username
            user_ok.xuan_stu_name =user.stu_name
            user_ok.xuan_pro_title = user.pro_title

            user_ok.save()

            models.Select_notok.objects.filter(notok_username=user.stu_username).delete()



    return redirect('/teacher/index/')

# 已经选题学生
def chakan_select(request):

    return render(request,'project/chakan_select.html')

def teacher_chakan(request):
    okusers_list = []

    ok_req = Select_Over.objects.all()

    for item in ok_req:
        user_info ={
            'xuan_username':item.xuan_username,
            'xuan_stu_name':item.xuan_stu_name,
            'xuan_pro_title':item.xuan_pro_title
        }
        okusers_list.append(user_info)
    okuser_dic = {}
    okuser_dic['data']=okusers_list
    return HttpResponse(json.dumps(okuser_dic))

# 尚未选题学生
def chakan_notok(request):

    return render(request,'project/chakannotok_select.html')

def tea_chakan(request):
    notusers_list = []
    not_req = Select_notok.objects.all()
    for items in not_req:
        uokuser_info ={
            'notok_username':items.notok_username,
            'notok_stu_name':items.notok_stu_name
        }
        notusers_list.append(uokuser_info)
    uokuser_dic = {}
    uokuser_dic['data']=notusers_list
    return HttpResponse(json.dumps(uokuser_dic))

def kaohe(request):
    if request.method == 'POST':
        kaohe_form = forms.KaoHeForm(request.POST)
        if kaohe_form.is_valid():
            stu_name = kaohe_form.cleaned_data['stu_name']
            kaoqin = kaohe_form.cleaned_data['kaoqin']
            baogao = kaohe_form.cleaned_data['baogao']
            shixian =kaohe_form.cleaned_data['shixian']

            neirong = models.KaoHe()
            neirong.stu_name=stu_name
            neirong.kaoqin = int(kaoqin)
            neirong.baogao = int(baogao)
            neirong.shixian = int(shixian)
            neirong.count = neirong.kaoqin*0.1+neirong.baogao*0.3+neirong.shixian*0.6

            neirong.save()

            return redirect('/teacher/index/')

    kaohe_form = forms.KaoHeForm
    return render(request,'project/count.html',locals())

def chakan_count(request):
    return render(request, 'project/chakancount.html')

def cha_count(requset):
    chengji = []
    username = requset.session.get('username')
    neirong = Student.objects.filter(username=username).all().first()
    stu_name = neirong.stu_name
    req = models.KaoHe.objects.filter(stu_name=stu_name).all()
    for item in req:
        user_info = {
            'kaoqin':item.kaoqin,
            'baogao':item.baogao,
            'shixian':item.shixian,
            'count':item.count,
        }
        chengji.append(user_info)
    user_dic = {}
    user_dic['data'] = chengji
    return HttpResponse(json.dumps(user_dic))

# def project_page(request,pro_id):
#     project = models.TeacherProject.objects.get(pro_id = pro_id)
#     return render(request,'project_page.html',{'project':project})