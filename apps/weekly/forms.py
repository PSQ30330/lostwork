from captcha.fields import CaptchaField
from django import forms


class StudentWeeklyForm(forms.Form):

    title = forms.CharField(label="标题",max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    plan_finish = forms.CharField(label="计划完成",max_length=5000, widget=forms.TextInput(attrs={'class': 'form-control'}))
    finished = forms.CharField(label="实际完成",max_length=5000, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='问题与计划',max_length=5000, widget=forms.TextInput(attrs={'class': 'form-control'}))

    captcha = CaptchaField(label='验证码')

class TeacherInputForm(forms.Form):
    username = forms.CharField(label="学号",max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

