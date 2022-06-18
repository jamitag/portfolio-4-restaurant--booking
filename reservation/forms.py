from django.forms import ModelForm
from django import forms
from .models import Reserve, User
import datetime as dt

HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]

# class DateInput(forms.DateInput):
#     input_type = 'date'

class ReservationForm(ModelForm):
    class Meta:
        model = Reserve
        fields = ['date', 'time', 'parties']
        widgets = {
            'time': forms.TextInput(attrs={'placeholder': '6 PM'}),
            'date': forms.DateInput(format=('%d-%m-%Y'), 
                                             attrs={'class':'form-control', 'type':'date', 
                                            'placeholder':'Select a date'}),
        }


        def __init__(self, *args, **kwargs):
            initial = kwargs.pop('initial', User)
            self.contact = kwargs.pop('contact')
            for key in self.fields:
                if hasattr(self.contact, key):
                    initial[key] = initial.get(key) or  getattr(self.person, key)
                kwargs['initial'] = initial
                super(Meta, self).__init__(*args, **kwargs)



