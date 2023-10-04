from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def login_user(request):
    # Check if logged in
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # Authentication
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.success(request, ("That did not work! Please try again"))
            return redirect('login')

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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        # Authentication
        user = authenticate(request, username=username, password=password)
        login(request, user)
        messages.success(request, ("Sign up successful!"))
        return redirect('index.html')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form, })
