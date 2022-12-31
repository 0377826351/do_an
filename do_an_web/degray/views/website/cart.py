from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect
from  ...models import Item,Cart


def index(request):
    template = loader.get_template('website/cart/cart.html')
    user = request.user
    list_cart = Cart.objects.filter(user_add=user.id)
    count = list_cart.count()
    total_price = 0
    for i in list_cart:
        total_price += i.price*i.qty

    if request.method == 'POST':
        new_qty = request.POST.get('qty')
        code = request.POST.get('slug')
        size = request.POST.get('item-size')
        item = Cart.objects.get(product_code=code,item_size = size)
        item.qty = new_qty
        item.save()
        return redirect("cart_index")
    context = {
        'title': 'Giỏ Hàng',
        'list_cart': list_cart,
        'count':count,
        'total_price': total_price,
    }
    return HttpResponse(template.render(context, request))

def delete(request,code,size):
    item = Cart.objects.get(product_code=code,item_size=size)
    item.delete()
    return HttpResponseRedirect(reverse('cart_index'))