from django.forms import ModelForm
from django import forms
from .models import Reserve
import datetime as dt

HOUR_CHOICES = [(None, 'Time')] + [
    (dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(12, 24)
    ]


class ReservationForm(ModelForm):
    class Meta:
        model = Reserve
        fields = ['date', 'time', 'parties']
        widgets = {
            'time': forms.Select(choices=HOUR_CHOICES),
            'date': forms.DateInput(format=('%d-%m-%Y'),
                                    attrs={'class': 'form-control',
                                    'type': 'date',
                                            'placeholder': 'Select a date'}),
        }
