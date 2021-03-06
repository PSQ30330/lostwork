from captcha.fields import CaptchaField
from django import forms


class ProForm(forms.Form):

    gender = (
        ('1', "校内"),
        ('2', "校外"),
    )

    pro_title = forms.CharField(label="标题",max_length=40,widget=forms.TextInput(attrs={'class': 'form-control'}))
    pro_type = forms.ChoiceField(label='课题类型',choices=gender)
    pro_content = forms.CharField(label='课题内容',max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    pro_count = forms.IntegerField(label="学生选题人数",widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')



class XuanTiForm(forms.Form):
    stu_proid = forms.CharField(label="实训题目id号",max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class KaoHeForm(forms.Form):
    stu_name = forms.CharField(label='学号',max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
    kaoqin = forms.CharField(label='考勤成绩',max_length=15,widget=forms.TextInput(attrs={'class': 'form-control'}))
    baogao = forms.CharField(label='报告成绩', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    shixian = forms.CharField(label='系统实现成绩', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')