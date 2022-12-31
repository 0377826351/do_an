from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect
from  ...models import Item,Cart,Receipt,Receipt_DeTail
from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        template = loader.get_template('website/pay/pay.html')
        list_cart = Cart.objects.filter(user_add=request.user)
        user = request.user
        count = list_cart.count()
        total_price = 0
        for i in list_cart:
            total_price += i.price*i.qty

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            note = request.POST.get('note')
            rec = Receipt(id_user=user.id,name_cus=name,email_cus=email,phone_cus=phone,address_cus=address,note=note)
            rec.save()
            # id_rec =rec.id
            for i in list_cart:
                rec_det = Receipt_DeTail(id_receipt=rec.id,name_item=i.item_name,item_size=i.item_size,qty_item=i.qty,price=i.price,image=i.image)
                rec_det.save()
            Cart.objects.all().delete()
            return HttpResponseRedirect(reverse('myorder_index'))
        context = {
            'title': 'Thanh Toán',
            'list_cart': list_cart,
            'count':count,
            'total_price': total_price,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/login")