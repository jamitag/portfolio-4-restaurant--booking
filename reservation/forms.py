from django.forms import ModelForm
from django import forms
from .models import reservation
import datetime as dt
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(ModelForm):
    class Meta:
        model = reservation
        fields = ['date', 'parties', 'contact']
        widgets = {
            'date': DateInput(), 
            'date': forms.Select(choices=HOUR_CHOICES),
        }