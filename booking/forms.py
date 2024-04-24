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

    def clean(self):
        cleaned_data = super(TableBookingForm, self).clean()
        table_number = cleaned_data.get('table_number')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        if Reservations.objects.filter(table=table, date=date, time=time, active_booking=True).exists():
            raise ValidationError("This table is already booked for that date and time")

        return cleaned_data