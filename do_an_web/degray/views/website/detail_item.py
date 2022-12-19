from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from  ...models import Item,Cart

def index(request,slug=None):
    template = loader.get_template('website/detail_item/detail_item.html')
    obj = Item.objects.get(product_code = slug)
    list_item = Item.objects.filter(category_item = obj.category_item)[:10]
    if request.method == 'POST':
        try:
            new_qty = request.POST.get('qty')
            item = Cart.objects.get(item_name=obj.name)
            cur_qty = item.qty
            total_qty = cur_qty + int(new_qty)
            item.qty = total_qty
            item.save()
        except Cart.DoesNotExist:
            new_qty = request.POST.get('qty')
            cart = Cart(user_add=request.user,item_name=obj.name,qty=new_qty,price=obj.price,image=obj.image)
            cart.save()
    context = {
        'title': 'Detail Item',
        'obj': obj,
        'list_item': list_item,
    }
    return HttpResponse(template.render(context, request))