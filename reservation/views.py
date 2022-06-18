from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Reserve
import datetime
from .forms import ReservationForm
import uuid

user = {}

"""
Provides data and functionality for the index screen
"""


def index(request):
    r = Reserve.objects.all()
    context = {
        'r': r
    }

    return render(request, 'index.html', context)


def login_page(request):
    context = {
        'user': user
    }

    user['username'] = 'random string'

    return render(request, 'login.html', context=context)


def sign_in(request):
    credentials = request.POST
    username = credentials.get('username')
    password = credentials.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, '')


"""
Creates a new reservation record
"""


def create_reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('Reservations')
    context = {'form': form}
    return render(request, 'reservation_form.html', context)


"""
Update reservation record
"""


def updateReservation(request, pk):
    reservation = Reserve.objects.get(id=pk)
    form = ReservationForm(instance=reservation)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('Reservations')
    context = {'form': form}
    return render(request, 'update_reservation_form.html', context)


"""
Delete reservation record
"""


def deleteReservation(request, pk):
    reservation = Reserve.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('Reservations')
    context = {'object': reservation}
    return render(request, 'delete.html', context)


def Reservations(request):
    reservations = {}
    context = {}
    if request.user:
        reservations = Reserve.objects.filter(author=request.user)
        context = {'reservations': reservations}

    return render(request, 'reservations.html', context)


def aboutUs(request):
    return render(request, 'about_us.html')


def menu(request):
    return render(request, 'menu.html')
