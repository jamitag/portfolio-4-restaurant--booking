from django.shortcuts import render
from .models import reservation, contact
import datetime

def index(request):
    reservations = reservation.objects.all()
    c = contact.objects.all()
    context = {
        'reservations': reservations,
        'add_reservation': add_reservation(c[0], 0)
    }

    return render(request, 'index.html', context=context)

def add_reservation(contact, parties):
    reservation.objects.create(contact=contact, date=datetime.datetime.now(), parties=parties)


