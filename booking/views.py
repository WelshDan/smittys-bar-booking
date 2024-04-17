from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Reservations
from .forms import TableBookingForm


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
        user_bookings = Reservations.objects.filter(email=request.user.email).filter(active_booking=True)
        if 'submitted' in request.GET:
            submitted = True
            active_booking = True
    return render(request, 'booktable.html', {'form':form, 'submitted':submitted, 'bookings': user_bookings})


def edit_reservation(request, booking_id):
    booking = get_object_or_404(Reservations, pk=booking_id)
    form = TableBookingForm(user=request.user, instance=booking)
    if request.method == "POST":
        form = TableBookingForm(request.POST, user=request.user, instance=booking)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/edit_reservation')
    return render(request, 'edit_reservation.html', {'form':form, 'booking':booking})


def delete_reservation(request, booking_id):
    booking = Reservations.objects.get(pk=booking_id)
    booking.delete()
    return redirect('booktable')


def get_bookings(request):
    bookings = Reservations.objects.filter(active_booking=True)
    return render(request, 'booktable.html', {'bookings': bookings})


def get_index(request):
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'account_signup.html')


def get_login(request):
    return render(request, 'account_login.html')
