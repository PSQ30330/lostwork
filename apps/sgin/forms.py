from captcha.fields import CaptchaField
from django import forms


class StudentSginForm(forms.Form):
    username = forms.CharField(label="学号", max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

