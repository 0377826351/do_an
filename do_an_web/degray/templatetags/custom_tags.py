# Create the register instance by initializing it with the Library instance.
from django.template.defaulttags import register
from django import template
register = template.Library()
from django.contrib.auth.models import User
from  ..models import Item,Cart,Receipt,Receipt_DeTail
from urllib import parse
from django.contrib.auth.decorators import login_required

@login_required
@register.inclusion_tag('website/templatetags/carttop.html', takes_context=True)
def show_cart(context):
    request = context['request']
    user = request.user
    print(user)
    if user.is_authenticated:
        list_cart = Cart.objects.filter(user_add=user)
        count = list_cart.count()
        total_price = 0
        for i in list_cart:
            total_price += i.price*i.qty
        return {'list_cart': list_cart,'count':count,'total_price':total_price}
    else:
        return {'list_cart': '','count':'0','total_price':'0'}

@register.filter(name="keyvalue")
def keyvalue(dict, key):    
    return dict[key]

@register.inclusion_tag('admin/templatetags/noti.html')
def noti(noti):
    print(noti)
    icon = {
        'danger':'ban',
        'info':'info',
        'warning':'exclamation-triangle',
        'success':'check',
    }
    return {'noti': noti, 'icon': icon}

@register.filter(name='total')
def total_price(id_rec):
    list_item = Receipt_DeTail.objects.filter(id_receipt=id_rec)
    total_price = 0
    for i in list_item:
        total_price += i.price*i.qty_item
    return total_price+30000

@register.filter(name='autoincrement')
def autoincrement(count):
    for i in range(count):
        print(i)



