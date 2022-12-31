from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def staff(request):
    template = loader.get_template('admin/staff/index.html')
    user = request.user
    is_super = user.is_superuser
    list_obj = User.objects.filter(is_staff=True,is_superuser=False)
    context = {
        'title': 'Staff',
        'list_obj': list_obj,
        'super':is_super,
    }
    return HttpResponse(template.render(context, request))

def delete(request,id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('staff_admin_index')