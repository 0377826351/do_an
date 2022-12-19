from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from  ...models import Item,Cart

def index(request):
    searched = request.GET.get('q')
    if not searched:
        template = loader.get_template('website/home/home.html')
        list_balo =Item.objects.filter(category_item_id=1)
        list_pants =Item.objects.filter(category_item_id=5)
        list_tshirt =Item.objects.filter(category_item_id=3)
        list_jacket =Item.objects.filter(category_item_id=2)
        list_bag =Item.objects.filter(category_item_id=4)
        context = {
            'title': 'Home',
            'list_balo': list_balo,
            'list_pants': list_pants,
            'list_tshirt': list_tshirt,
            'list_jacket': list_jacket,
            'list_bag': list_bag,
        }
        return HttpResponse(template.render(context, request))
    else:
        list_item = Item.objects.filter(name__icontains=searched)
        template = loader.get_template('website/items/items.html')
        context = {
            'title': 'Home',
            'list_item':list_item,
        }
        return HttpResponse(template.render(context, request))
