from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator
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
    
    paginator = Paginator(list_item, 8)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    context = {
            'title': 'Items',
            'slug':slug,
            'page_obj': page_obj,
            # 'page_range': page_obj.paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=1)
        }

    return HttpResponse(template.render(context, request))

