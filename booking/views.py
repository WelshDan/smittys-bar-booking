from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reservations
from .forms import TableBookingForm


def get_base(request):
    return render(request, 'base.html')


def reserve_table(request):
    submitted = False
    active_booking = False
    form = TableBookingForm()
    user_bookings = Reservations.objects.filter(email=request.user.email).filter(active_booking=True)
    
    if request.method == "POST":
        form = TableBookingForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,
                "Congratulations you have booked a table. See YOUR RESERVATIONS for details.")
            return HttpResponseRedirect('/booktable')
    else:
        form = TableBookingForm(user=request.user)
        if 'submitted' in request.GET:
            submitted = True
            active_booking = True
    return render(request, 'booktable.html', {'form':form, 'submitted':submitted, 'bookings': user_bookings})


def edit_reservation(request, booking_id):
    user_bookings = Reservations.objects.filter(email=request.user.email).filter(active_booking=True)
    booking = Reservations.objects.get(pk=booking_id)
    form = TableBookingForm(user=request.user, instance=booking)
    if request.method == "POST":
        form = TableBookingForm(request.POST, user=request.user, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has now been updated. See YOUR RESERVATIONS for details.")
            return redirect('booktable')
    return render(request, 'edit_reservation.html', {'form':form, 'booking':booking, 'bookings': user_bookings})


def delete_reservation(request, booking_id):
    booking = Reservations.objects.get(pk=booking_id)
    booking.delete()
    messages.success(request, "Your booking has now been deleted.")
    return redirect('booktable')


@login_required
def get_bookings(request):
    if request.user.is_superuser:
        bookings = Reservations.objects.all()
    else:
        bookings = Reservations.objects.filter(email=request.user.email, active_booking=True)
    return render(request, 'booktable.html', {'bookings': bookings})


def get_index(request):
    return render(request, 'index.html')


def get_signup(request):
    return render(request, 'account_signup.html')


def get_login(request):
    return render(request, 'account_login.html')
