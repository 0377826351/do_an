from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from  ...models import Item

def index(request,slug=None,ft=None):
    template = loader.get_template('website/items/items.html')
    context = {}
    # if ft is not None:
    if slug is None:
        list_item =Item.objects.all()
        if ft=="a-z":
            list_item = list_item.order_by('name')              
        elif ft=="z-a":
            list_item = list_item.order_by('-name')              
        elif ft == "price-up":
            list_item = list_item.order_by('price')
        elif ft == "price-down":
            list_item = list_item.order_by('-price')
    else:
        list_item = Item.objects.filter(category_item_id=slug)
        if ft=="a-z":
            list_item = list_item.order_by('name')              
        elif ft=="z-a":
            list_item = list_item.order_by('-name')              
        elif ft == "price-up":
            list_item = list_item.order_by('price')
        elif ft == "price-down":
            list_item = list_item.order_by('-price')


    context = {
            'title': 'Items',
            'list_item':list_item,
            'slug':slug
        }

    return HttpResponse(template.render(context, request))

