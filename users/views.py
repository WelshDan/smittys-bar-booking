from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("That did not work! Try again please"))
            return redirect('login')

    else:
        return render(request, 'registration/login.html', {})
