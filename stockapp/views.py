# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # เปลี่ยนไปที่หน้าหลักหลังจากล็อกอิน
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # หลังจากลงทะเบียนเสร็จ จะไปที่หน้า login
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'home.html')