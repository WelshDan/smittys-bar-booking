from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from booking.models import Reservations
from crispy_forms.helper import FormHelper
from users.models import Customers

class TableBookingForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Reservations
        fields = ('email', 'table_number', 'date', 'start_time', 'end_time')
        widgets = {
            "date": DatePickerInput(options={"format": "DD/MM/YYYY"}),
            "start_time": TimePickerInput(options={
                "format": "HH:MM",
                "minHour": 12,
                "maxHour": 23,
            }),
            "end_time": TimePickerInput(options={"format": "HH:MM"}),
        }

    def __init__ (self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['email'].initial = user.email