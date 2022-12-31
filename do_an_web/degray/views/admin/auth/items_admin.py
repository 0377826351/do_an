from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
# from ....forms import ArtForm
from ....models import Item,Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def items(request):
    template = loader.get_template('admin/items/index.html')
    list_obj = Item.objects.all()
    context = {
        'title': 'Items',
        'list_obj': list_obj,
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_item(request):
    template = loader.get_template('admin/items/add.html')
    user = request.user
    list_cate = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        product_code = request.POST.get('product_code')
        price = request.POST.get('price')
        detail = request.POST.get('detail')
        cate = request.POST.get('cate')
        image = request.FILES['image']
        new_item = Item(name=name,product_code=product_code,price=price,detai=detail,category_item_id=cate,created=request.user,image=image)
        new_item.save()
        return redirect('items_admin_index')
    context = {
        'title': 'Add Item',
        'list_cate':list_cate,
    }
    return HttpResponse(template.render(context, request))


@login_required
def update_item(request, id):
    template = loader.get_template('admin/items/update.html')
    item = Item.objects.get(id=id)
    list_cate = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        product_code = request.POST.get('product_code')
        price = request.POST.get('price')
        detail = request.POST.get('detail')
        cate = request.POST.get('cate')
        print(cate)
        try:
            image = request.FILES['image']
        except:
            image = item.image
        item.name=name
        item.product_code=product_code
        item.price = price
        item.detail=detail
        item.category_item_id=cate
        item.image=image
        item.save()
        return redirect('items_admin_index')
    context = {
        'title':"Update Item",
        'list_cate':list_cate,
        'item':item,
    }
    return HttpResponse(template.render(context, request))

@login_required
def delete_item(request, id):
    item = Item.objects.get(id = id)
    item.delete()
    return redirect('staff-admin_index')

