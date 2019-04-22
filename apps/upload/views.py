from django import forms
from django.http import HttpResponse
from django.shortcuts import render





# Create your views here.
from upload.models import Files


class UserForm(forms.Form):
    title = forms.CharField()
    headfiles = forms.FileField()


def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            title = uf.cleaned_data['title']
            headfiles =uf.cleaned_data['headfiles']
            user = Files()
            user.title =title
            user.headfiles = headfiles
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render(request, 'upload/register.html',locals())