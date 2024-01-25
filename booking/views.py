from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Reservations
from .forms import TableBookingForm


def get_base(request):
    return render(request, 'base.html')


def get_booktable(request):
    return render(request, 'booktable.html')


def reserve_table(request):
    submitted = False
    form = TableBookingForm(request.POST)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reserve_table?submitted=True')
    else:
        form = TableBookingForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'booktable.html', {'form':form, 'submitted':submitted})


def get_index(request):
    messages.success(request, ("That did not work! Please try again"))
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'account_signup.html')


def get_login(request):
    return render(request, 'account_login.html')
