from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from  ...models import Customer

def index(request):
    template = loader.get_template('website/home/home.html')
    return HttpResponse(template.render({'title': 'Home'}, request))

    