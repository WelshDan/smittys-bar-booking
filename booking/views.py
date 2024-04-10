from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from booking.models import Reservations
from booking.forms import TableBookingForm


def get_base(request):
    return render(request, 'base.html')


def reserve_table(request):
    submitted = False
    active_booking = False
    form = TableBookingForm()
    
    if request.method == "POST":
        form = TableBookingForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reserve_table?submitted=True')
    else:
        form = TableBookingForm(user=request.user)
        if 'submitted' in request.GET:
            submitted = True
            active_booking = True
    return render(request, 'booktable.html', {'form':form, 'submitted':submitted})


def get_index(request):
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'account_signup.html')


def get_login(request):
    return render(request, 'account_login.html')
