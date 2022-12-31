from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django import forms
from ....models import Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def category(request):
    template = loader.get_template('admin/category/index.html')
    list_obj = Category.objects.all()
    context = {
        'title': 'Category',
        'list_obj': list_obj,
    }
    return HttpResponse(template.render(context, request))

@login_required
def add(request):
    template = loader.get_template('admin/category/add.html')
    list_obj = Category.objects.all()
    if request.method == 'POST':
        alias_category = request.POST.get('alias_category')
        name = request.POST.get('name')
        active = request.POST.get('active')
        if active == "on":
            new_cate = Category(alias_category=alias_category, name=name, active=1)
        else:
            new_cate = Category(alias_category=alias_category, name=name, active=0)
        new_cate.save()
        return redirect('category_admin_index')
    context = {
        'title': 'Add Category',
        'list_obj': list_obj,
    }
    return HttpResponse(template.render(context, request))

@login_required
def update(request, id=id):
    template = loader.get_template('admin/category/update.html')
    cate = Category.objects.get(id=id)
    if request.method == 'POST':
        alias_category = request.POST.get('alias_category')
        name = request.POST.get('name')
        active = request.POST.get('active')
        print(active)
        if active == "on":
            active = 1
        else:
            active = 0
        print(active)
        cate.alias_category = alias_category
        cate.name = name
        cate.active = active
        cate.save()
        return redirect('category_admin_index')
    context = {
        'title': 'Update Category',
        'cate':cate,
        }
    return HttpResponse(template.render(context, request))


def delete(request,id):
    cate = Category.objects.get(id = id)
    cate.delete()
    return redirect('category_admin_index')