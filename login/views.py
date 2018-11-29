from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.utils import timezone
# Create your views here.
from login import models
from login import forms
from utils import common
import datetime



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
                if not user.has_confirmed:
                    message = "该用户还未通过邮件确认！"
                    return render(request,'login/login.html',locals())
                if user.password == common.hash_code(password):
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
    if request.session.get('is_login',None):
        return redirect("/index")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入的密码不一致"
                return render(request,"login/register.html",locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = "用户已存在，请重新设置用户名"
                    return render(request,'login/register.html',locals())


                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = "该邮箱地址已被注册，请登录"
                    return redirect('/login')

                new_user = models.User()
                new_user.name = username
                new_user.password = common.hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = common.make_confirm_string(new_user)
                common.send_email(email,code)

                message = "请前往注册邮箱，进行邮箱确认！"
                return render(request,'login/confirm.html',locals())

    register_form = forms.RegisterForm()

    return render(request,'login/register.html',locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")
    request.session.flush()
    return redirect('/index/')

def user_confirm(request):
    code = request.GET.get('code',None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = "无效的确认请求！"
        return render(request,'login/confirm.html',locals())

    c_time = confirm.c_time
    # now = datetime.datetime.now()
    now = timezone.now()
    if now > c_time + datetime.timedelta(days=settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册'
        return render(request,'login/register.html',locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = "感谢确认，请使用账户登录"
        return render(request,'login/confirm.html',locals())









