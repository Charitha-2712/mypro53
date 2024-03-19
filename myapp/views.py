from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from . forms import RegisterForm
from . forms import LoginForm


# Create your views here.

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def trainers(request):
    return render(request,'trainers.html')

def about(request):
    return render(request,'about.html')

def enquiry(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponse("<h1>Registration was sucessful</h1>")
    f = RegisterForm()
    return render(request,'enquiry.html',context={'form':f})


def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect(reverse('myapp:home'))
            else:
                messages.info(request,'Username or password is not valid')
                return redirect('/login/')
    f=LoginForm()
    return render(request,'login.html',context={'form':f})    


def logout_view(request):
    logout(request)
    return redirect(reverse('myapp:login'))     
  



