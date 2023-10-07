from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class TableBookings(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())
    
