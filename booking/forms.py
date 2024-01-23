from django import forms
from django.forms import ModelForm
from .models import Reservations


class TableBookingForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('table_number', 'date', 'start_time', 'end_time')
