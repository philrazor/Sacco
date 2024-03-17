from django.shortcuts import render
from .models import user 
# Create your views here.

def home(request):
    user_all = user.objects.all()
    return render(request , 'core/home.html' , {'user_all' : user_all})

def form(request):
    return render(request , 'core/form.html')

def about(request):
    return render(request , 'core/about.html')
