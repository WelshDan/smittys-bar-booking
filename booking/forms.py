from django import forms
from booking.models import Reservations
from users.models import Customers
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class TableBookingForm(forms.ModelForm):
    email = forms.EmailField()
    date = forms.DateField(widget=DatePickerInput)
    start_time = forms.TimeField(widget=TimePickerInput)
    end_time = forms.TimeField(widget=TimePickerInput)

    class Meta:
        model = Reservations
        fields = ('email', 'table_number', 'date', 'start_time', 'end_time')

    def __init__ (self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['email'].initial = user.email