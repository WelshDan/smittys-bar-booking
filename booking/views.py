from .models import Reservations
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import TableBookingForm

def get_base(request):
    return render(request, 'base.html')


def get_booktable(request):
    return render(request, 'booktable.html')


def get_index(request):
    messages.success(request, ("That did not work! Please try again"))
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'signup.html')


def get_login(request):
    return render(request, 'login.html')

