from django.shortcuts import render
from .models import reservation, contact
import datetime
from django.contrib.auth.models import User

"""
Provides data and functionality for the index screen
"""

def index(request):
    # request.user = User.objects.all()[0]
    # currentuser = User.objects.all()[0]
    c = contact.objects.get(first_name='Harry')
    reservations = reservation.objects.filter(contact=c)
    context = {
        'reservations': reservations,
        'add_reservation': add_reservation(c, 0)
    }

    return render(request, 'index.html', context=context)

def login(request):
    context = {}
    return render(request, 'login.html', context=context)


"""
Creates a new reservation record
"""

def add_reservation(contact, parties):
    reservation.objects.create(contact=contact, date=datetime.datetime.now(), parties=parties)


