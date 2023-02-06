from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime
from users.models import WelcomePage

def index(request):
    welcome = WelcomePage.objects.all()
    context = {'welcome':welcome}
    return render(request, 'index.html', context=context)

def about_us(request):
    return render(request, 'about_us.html', context={})