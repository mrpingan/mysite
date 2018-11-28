from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from login import models
from login import forms

def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)

                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在"
                # return redirect('/register/')
        return render(request,'login/login.html',locals())
    login_form = forms.UserForm()
    return render(request,'login/login.html',locals())

def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")
    request.session.flush()
    return redirect('/index/')
