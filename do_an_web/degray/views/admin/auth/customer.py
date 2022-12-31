from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from ....models import Receipt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def customer(request):
    template = loader.get_template('admin/customer/index.html')
    user = request.user
    is_super = user.is_superuser
    is_staff = user.is_staff
    list_obj = User.objects.filter(is_staff=False,is_superuser=False)
    context = {
        'title': 'Customer',
        'list_obj': list_obj,
        'super':is_super,
        'staff':is_staff,
    }
    return HttpResponse(template.render(context, request))

def delete(request,id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('customer_admin_index')