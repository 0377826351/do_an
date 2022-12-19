# Create the register instance by initializing it with the Library instance.
from django.template.defaulttags import register
from django import template
register = template.Library()
from django.contrib.auth.models import User
from  ..models import Item,Cart
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
            total_price += i.price
        return {'list_cart': list_cart,'count':count,'total_price':total_price}
    else:
        return {'list_cart': '','count':'0','total_price':'0'}

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


