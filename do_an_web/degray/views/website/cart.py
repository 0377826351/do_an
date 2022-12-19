from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from  ...models import Item,Cart


def index(request):
    template = loader.get_template('website/cart/cart.html')
    list_cart = Cart.objects.filter(user_add=request.user)
    count = list_cart.count()
    total_price = 0
    for i in list_cart:
        total_price += i.price
    context = {
        'title': 'Giỏ Hàng',
        'list_cart': list_cart,
        'count':count,
        'total_price': total_price,
    }
    return HttpResponse(template.render(context, request))