from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from  ...models import Item,Cart
from django.contrib.auth import authenticate


def login(request):
    template = loader.get_template('website/user/login.html')

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            context={
                'title': 'Login',
                'error':'success',
                'user':user,
            }
            return redirect("/home")
        else:
            context={
                'title': 'Login',
                'error':'Sai tài khoản hoặc mật khẩu'
            }
    else:
        context = {
            "title": "Login"
        }
    return HttpResponse(template.render(context, request))

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/home')

def register(request):
    template = loader.get_template('website/user/register.html')
    if request.method == 'POST':
        fullName = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        passWord = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")
        if passWord == confirmPassword:
            user = User(last_name=fullName,username=username,email=email,is_superuser=False,is_staff=False)
            user.set_password(passWord)
            user.save()
            return redirect('/login')
        else:
            context={
                'title': 'Register',
                'error':'Mật khẩu không trùng khớp'
            }
    else:
        context = {
            "title": "Register"
        }
    return HttpResponse(template.render(context, request))

def changePassword(request):
    template = loader.get_template('website/user/change_password.html')
    user =request.user
    if user.is_anonymous:
        return redirect("/home")
    elif request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        if new_password == confirm_new_password and user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            context = {
                'title': 'Change Password',
                'noti':' Đổi mật khẩu thành công!'
            }
        elif new_password != confirm_new_password:
            context = {
                'title': 'Change Password',
                'noti':' Mật khẩu hiện tại không đúng!'
            }
        else:
            context = {
                'title': 'Change Password',
                'noti':' Mật khẩu không trùng khớp!'

            }
    else:
        context = {
            'title':  'Change Password',
        }
    return HttpResponse(template.render(context, request))


def forgotPassword(request):
    template = loader.get_template('website/user/forgot_password.html')
    context = {}
    return HttpResponse(template.render(context, request))
    