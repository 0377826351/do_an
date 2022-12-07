from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from  ...models import Customer

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
    logout(request)
    return redirect('/login')

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
    pass

def forgotPassword(request):
    pass