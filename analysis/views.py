from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'analyticsdash/index.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("You've error logging in check your username and password!"))
            return redirect('login')
    else:
        return render(request,'analyticsdash/login.html',{})

def logout_user(request):
    logout(request)
    # messages.success(request,("You've Succcesfully Logged Out!"))
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username,email=email,password=password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('register')
    else:
        return render(request,'analyticsdash/register.html',{})
