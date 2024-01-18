from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    # Check if logging in
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # Authentication
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, ("That did not work! Please try again"))
            return redirect('login')
            
    else:
        return render(request, 'allauth/account/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out"))
    return redirect('index')


def signup_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authentication
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, ("Sign up successful!"))
        return redirect('index')
    else:
        form = RegisterForm()

    return render(request, 'allauth/account/signup.html', {'form': form})


def get_index(request):
    messages.success(request, ("That did not work! Please try again"))
    return render(request, 'index.html')


def get_booktable(request):
    return render(request, 'booktable.html')

    
def get_base(request):
    return render(request, 'base.html')


def get_signup(request):
    return render(request, 'signup.html')


def get_login(request):
    return render(request, 'login.html')