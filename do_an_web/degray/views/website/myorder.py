from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from  ...models import Receipt,Receipt_DeTail
from django.shortcuts import render,redirect

def index(request):
    template = loader.get_template('website/myorder/myorder.html')
    user = request.user
    list_rec = Receipt.objects.filter(id_user = user.id).order_by("-created_at")
    tuples = Receipt.status.field.choices
    list_status = dict((y, x) for y, x in tuples)
    list_rec_det = Receipt_DeTail.objects.all()
    count = list_rec.count()
    context = {
        'title': 'Đơn Hàng của tôi',
        'list_rec': list_rec,
        'count': count,
        'list_rec_det': list_rec_det,
        'list_status': list_status,

    }
    return HttpResponse(template.render(context, request))

def delete(request,id):
    rec = Receipt.objects.get(id = id)
    rec.status = 4
    rec.save()
    return redirect('myorder_index')
