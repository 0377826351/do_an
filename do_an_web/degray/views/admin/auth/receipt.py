from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from ....models import Receipt_DeTail,Receipt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# def index(request):
#     template = loader.get_template('website/myorder/myorder.html')
#     user = request.user
#     list_rec = Receipt.objects.filter(id_user = user.id)
#     # print(list_rec)
#     list_rec_det = Receipt_DeTail.objects.all()
#     count = list_rec.count()
#     context = {
#         'title': 'Đơn Hàng của tôi',
#         'list_rec': list_rec,
#         'count': count,
#         'list_rec_det': list_rec_det,
#     }
#     return HttpResponse(template.render(context, request))

@login_required
def receipt(request):
    template = loader.get_template('admin/receipt/index.html')
    user = request.user
    list_rec = Receipt.objects.all()
    list_rec_det = Receipt_DeTail.objects.all()
    tuples = Receipt.status.field.choices
    list_status = dict((y, x) for y, x in tuples)
    count = list_rec.count()
    context = {
        'title': 'Receipt',
        'list_rec': list_rec,
        'count': count,
        'list_status': list_status,
        'list_rec_det': list_rec_det,
    }
    return HttpResponse(template.render(context, request))

@login_required
def update_receipt(request,id):
    template = loader.get_template('admin/receipt/update.html')
    tuples = Receipt.status.field.choices
    list_status = dict((y, x) for y, x in tuples)
    rec = Receipt.objects.get(id=id)
    if request.method == 'POST':
        status = request.POST.get('status')
        try: 
            rec = Receipt.objects.get(id = id)
            rec.status = status
            rec.save()
            context = {
                'title': 'Update Receipt',
                'noti': 'Sửa thành công!',
            }
        except:
            context = {
                'title': 'Update Receipt',
                'noti': 'Sửa thất bại!'
            }
        return redirect('receipt_admin_index')
    else:
        context = {
            'title': 'Update Receipt',
            'rec': rec,
            'list_status': list_status,
    }
    return HttpResponse(template.render(context, request))

# @login_required
# def add_Receipt(request):
#     template = loader.get_template('admin/Receipt/add.html')
#     if request.method == 'POST':
#         Receipt = request.POST.get('Receipt')
#         answer = request.POST.get('answer')
#         try: 
#             Receipt = Receipt.objects.get(Receipt = Receipt)
#             context = {
#                 'title': 'Add Category',
#                 'noti': 'Câu hỏi tồn tại!'
#             }
#         except:
#             new_ques = Receipt(Receipt = Receipt,answer = answer)
#             new_ques.save()
#             context = {
#                 'title': 'Add Category',
#                 'noti': 'Thêm thành công!'
#             }
#     else:
#         context = {
#             'title': 'Add Receipt',
#     }
#     return HttpResponse(template.render(context, request))

@login_required
def delete_rec(request, id):
    ques = Receipt.objects.get(id = id)
    ques.delete()
    return redirect('receipt_admin_index')