from django.forms import ModelForm
from django import forms
from .models import reservation

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(ModelForm):
    class Meta:
        model = reservation
        fields = ['date', 'parties', 'contact']
        widgets = {
            'date': DateInput(), 
        }