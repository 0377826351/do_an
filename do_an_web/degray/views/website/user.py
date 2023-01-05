from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from  ...models import Item,Cart,Extend_User
from django.contrib.auth import authenticate
from datetime import datetime
from django.utils import timezone
import hashlib
import string
import random
import uuid
from ...helpers import send_forget_password_email
from django.contrib import messages


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
            return redirect("/")
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
        return redirect('/')

def register(request):
    template = loader.get_template('website/user/register.html')
    if request.method == 'POST':
        context = {}
        fullName = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        passWord = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")
        check_username = User.objects.filter(username=username).count()
        check_email = User.objects.filter(email=email).count()
        if check_username == 0 and check_email == 0:
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
                'title':'Register',
                'error':'Email or Username is exist'
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
        return redirect("/")
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
    context ={}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            time_now = timezone.now()
            time_hash = hashlib.sha256(str(time_now).encode('utf-8')).hexdigest()
            token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
            try:
                extend_user = Extend_User.objects.get(user_id = user.id)
                extend_user.token = token
                extend_user.token_date = time_now
                extend_user.save()
            except:
                new_extend_user = Extend_User(token = token,token_date = time_now,user_id = user.id)
                new_extend_user.save()
            return redirect("reset_password_user_done_index",id = user.id,token = token,token_date = time_hash)
        except:
            context = {
                'title': 'Recover PassWord',
                'error':'Sai Email'
            }
    else:
        context = {
            'title': 'Recover PassWord'
        }
    return HttpResponse(template.render(context, request))

def reset_password_confirm_user(request,id,token,token_date):
    template = loader.get_template('website/user/password_reset_success.html')
    extend = Extend_User.objects.get(user_id = id   )
    token_date_extend = extend.token_date
    if( timezone.now() - token_date_extend).seconds <300:
        if request.method == 'POST':
            new_password = request.POST.get('password')
            confirm = request.POST.get('confirmPassword')
            user = User.objects.get(id=id)
            if new_password  == confirm:
                user.set_password(new_password)
                user.save()
                user = authenticate(username=user.username, password=new_password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('/')
                else:
                    context = {
                    "title": "Confirm PassWord",
                    'error':'Mật khẩu không trùng khớp'
                    }
            else:
                context = {
                    "title": "Confirm PassWord",
                    'error':'Mật khẩu không trùng khớp'
                }
        else:
            context = {
                "title": "Confirm PassWord"
            }
    else:
        return redirect('/forgot-password')
    return HttpResponse(template.render(context,request))


# def changeps (request,token):
#     template = loader.get_template('website/user/password_reset_success.html')
#     context = {}
#     try:
#         profile_obj = Extend_User.objects.get(token = token)
#         print(profile_obj)
#     except Exception as e:
#         print(e)
#     return HttpResponse(template.render(context,request))


# def Forget_Password(request):
#     template = loader.get_template('website/user/forgot_password.html')
#     context = {
#     }
#     try:
#         if request.method == 'POST':
#             email = request.POST.get('email')
#             user = User.objects.get(email=email)
#             token = str(uuid.uuid4())
#             send_forget_password_email(user,token)
#             print(send_forget_password_email)
#             context = {
#                 'title': 'Recover PassWord',
#                 'error':'an email is sent'
#             }
#             return redirect('/forgot-password')
    
#     except Exception as e:
#         print(e)
    
#     return HttpResponse(template.render(context, request))

