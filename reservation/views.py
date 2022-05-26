from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import reservation, contact
import datetime
from .forms import ReservationForm

user = {}

"""
Provides data and functionality for the index screen
"""


def index(request):
    # request.user = User.objects.all()[0]
    reservations = {}
    c = contact.objects.all()[0]
    try:
        c = contact.objects.get(user=request.user)
        reservations = reservation.objects.filter(contact=c)
    except:
        print('')
    context = {
        'reservations': reservations,
        'add_reservation': add_reservation(c, 0)
    }

    return render(request, 'index.html', context=context)


def login_page(request):
    context = {
        # 'sign_in': sign_in(request),
        'user': user
    }

    user['username'] = 'random string'

    return render(request, 'login.html', context=context)


"""
Creates a new reservation record
"""


def add_reservation(contact, parties):
    reservation.objects.create(contact=contact, date=datetime.datetime.now(), parties=parties)


def sign_in(request):
    credentials = request.POST
    username = credentials.get('username')
    password = credentials.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, '')

# def sign_in():
#     print('')

def create_reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'reservation_form.html', context)