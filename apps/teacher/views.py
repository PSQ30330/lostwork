from django.shortcuts import render

# Create your views here.
import datetime
import hashlib

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect

from lostwork import settings
from teacher import forms, models


def index(request):

    return render(request, 'teacher/index.html')



def login(request):
    if request.session.get('is_login', None):
        return redirect("/teacher/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Teacher.objects.get(username=username)
                if not user.has_confirmed:
                    message = "该用户还未通过邮件确认！"
                    return render(request, 'teacher/login.html', locals())
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['username'] = user.username
                    request.session['tea_name'] = user.tea_name
                    return redirect('/teacher/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'teacher/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'teacher/login.html', locals())


def make_confirm_string(teacher):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(teacher.username, now)
    models.ConfirmString.objects.create(code=code, teacher=teacher )
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
                        <p>感谢注册<a href="http://{}/teacher/confirm/?code={}" target=blank>实训管理系统</a>
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
            tea_name = register_form.cleaned_data['tea_name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            emali = register_form.cleaned_data['emali']
            sex = register_form.cleaned_data['sex']

            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'teacher/register.html', locals())
            else:
                same_name_user = models.Teacher.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'teacher/register.html', locals())
                same_email_user = models.Teacher.objects.filter(emali=emali)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'teacher/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.Teacher()
                new_user.username = username
                new_user.tea_name = tea_name
                new_user.password = hash_code(password1)
                new_user.emali = emali
                new_user.sex = sex


                new_user.save()

                code = make_confirm_string(new_user)
                send_email(emali, code)

                return render(request,'teacher/register_successful.html')
    register_form = forms.RegisterForm()
    return render(request, 'teacher/register.html', locals())



def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/teacher/index/")
    request.session.flush()
    return redirect("/teacher/index/")

def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'teacher/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()


    confirm.teacher.has_confirmed = True
    confirm.teacher.save()
    confirm.delete()
    message = '激活成功，请使用账户登录！'
    return render(request, 'teacher/confirm.html', locals())