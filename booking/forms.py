from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from .models import Reservations
from django import forms
from crispy_forms.helper import FormHelper

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('table_number', 'date', 'start_time', 'end_time')
        widgets = {
            "name": forms.HiddenInput(),
            "date": DatePickerInput(options={"format": "MM/DD/YYYY"}),
            "start_time": TimePickerInput(),
            "end_time": TimePickerInput(range_from="start_time"),
        }
        