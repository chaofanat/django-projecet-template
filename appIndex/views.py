from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import application


def index(request):
    app_list = application.objects.filter(is_active=True)
    
    return render(request, 'appIndex/index.html' , {'app_list': app_list})