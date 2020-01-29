from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'analyticsdash/index.html')

def login(request):
    return render(request,'analyticsdash/login.html')

def register(request):
    return render(request,'analyticsdash/register.html')
