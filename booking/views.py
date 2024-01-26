from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from booking.models import Reservations
from booking.forms import TableBookingForm


def get_base(request):
    return render(request, 'base.html')


def reserve_table(request):
    print("reserve_table ok")
    submitted = False
    active_booking = False
    form = TableBookingForm()
    
    if request.method == "POST":
        form = TableBookingForm(request.POST)
        print("If request.method ok")
        if form.is_valid():
            form.save()
            print("if form.is_valid ok")
            return HttpResponseRedirect('/reserve_table?submitted=True')
    else:
        form = TableBookingForm()
        print("form = TableBookingForm ok")
        if 'submitted' in request.GET:
            print("if 'submitted' in request.GET ok")
            submitted = True
            active_booking = True
    return render(request, 'booktable.html', {'form':form, 'submitted':submitted})


def get_index(request):
    messages.success(request, ("That did not work! Please try again"))
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'account_signup.html')


def get_login(request):
    return render(request, 'account_login.html')
