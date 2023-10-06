from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    # Check if logged in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authentication
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.success(request, ("That did not work! Please try again"))
            return render(request, 'registration/login.html', {})

    else:
        return render(request, 'registration/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out"))
    return redirect('index')


def signup_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authentication
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Sign up successful!"))
        return redirect('index.html')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form, })
