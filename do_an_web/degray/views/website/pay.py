from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from  ...models import Item,Cart
from django.shortcuts import render

def index(request):
    template = loader.get_template('website/pay/pay.html')
    list_cart = Cart.objects.filter(user_add=request.user)
    count = list_cart.count()
    total_price = 0
    for i in list_cart:
        total_price += i.price
    context = {
        'title': 'Thanh Toán',
        'list_cart': list_cart,
        'count':count,
        'total_price': total_price,
    }
    return HttpResponse(template.render(context, request))