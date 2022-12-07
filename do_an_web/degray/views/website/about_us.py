from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

def index(request):
    template = loader.get_template('website/about_us/about_us.html')
    return HttpResponse(template.render({'title': 'Về chúng tôi'}, request))