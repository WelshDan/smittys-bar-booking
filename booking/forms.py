from django import forms
from .models import Reservations
from bootstrap_datepicker_plus.widgets import DatePickerInput

class TableBookingForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('table_number', 'start_time', 'end_time')
        widgets = {
                "date": DatePickerInput()
            }