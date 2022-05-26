from django.forms import ModelForm

from .models import reservation

class ReservationForm(ModelForm):
    class Meta:
        model = reservation
        fields = ['date', 'parties', 'contact']