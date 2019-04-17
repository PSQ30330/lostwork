import datetime
import hashlib

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect

from lostwork import settings
from student import forms
from student import models


def index(request):

    return render(request, 'student/index.html')



def login(request):
    if request.session.get('is_login', None):
        return redirect("/student/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Student.objects.get(username=username)
                if not user.has_confirmed:
                    message = "该用户还未通过邮件确认！"
                    return render(request, 'student/login.html', locals())
                if user.password == hash_code(password):
                    request.session['is_login'] = True

                    request.session['stu_name'] = user.stu_name
                    return redirect('/student/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'student/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'student/login.html', locals())


def make_confirm_string(student):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(student.username, now)
    models.ConfirmString.objects.create(code=code, student=student )
    return code

def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()



def send_email(emali, code):


    subject = '欢迎加入实训管理系统'

    text_content = '''感谢注册实训管理系统！\
                        如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                        <p>感谢注册<a href="http://{}/student/confirm/?code={}" target=blank>实训管理系统</a>
                        </p>
                        <p>请点击站点链接完成注册确认！</p>
                        <p>此链接有效期为{}天！</p>
                        '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [emali])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。
        return redirect("/index/")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            stu_name = register_form.cleaned_data['stu_name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            emali = register_form.cleaned_data['emali']
            sex = register_form.cleaned_data['sex']
            major = register_form.cleaned_data['major']
            stu_class = register_form.cleaned_data['stu_class']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'student/register.html', locals())
            else:
                same_name_user = models.Student.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'student/register.html', locals())
                same_email_user = models.Student.objects.filter(emali=emali)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'student/register.html', locals())



                new_user = models.Student()
                new_user.username = username
                new_user.stu_name = stu_name
                new_user.password = hash_code(password1)
                new_user.emali = emali
                new_user.sex = sex
                new_user.major = major
                new_user.stu_class = stu_class

                new_user.save()


                code = make_confirm_string(new_user)
                send_email(emali, code)

                return redirect('/student/login/')  # 自动跳转到登录页面
    register_form = forms.RegisterForm()
    return render(request, 'student/register.html', locals())



def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/student/index/")
    request.session.flush()


    return redirect("/student/index/")
def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'student/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()

    confirm.student.has_confirmed = True


    confirm.student.save()
    confirm.delete()
    message = '感谢确认，请使用账户登录！'
    return render(request, 'student/confirm.html', locals())

