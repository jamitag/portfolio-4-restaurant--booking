from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Reserve, Menu, AboutUs, Index, bgImage, RatingImage
from .forms import ReservationForm


user = {}

"""
Provides data and functionality for the index screen
"""


def index(request):
    index = Index.objects.all()
    img = RatingImage.objects.get()
    context = {'index': index, 'img': img }
    return render(request, 'index.html', context)

def base(request):
    bg_image = bgImage.objects.get()
    context = {'bg_image': bg_image, }
    return render(request, 'base.html', context)


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
            return redirect('ReservationsSuccess', pk='y')
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


"""
List of reservations for a user
"""


def Reservations(request, pk=''):
    reservations = {}
    context = {}
    if request.user:
        reservations = Reserve.objects.filter(author=request.user)
        context = {'reservations': reservations, 'success': pk}

    pk = ''

    return render(request, 'reservations.html', context)


def aboutUs(request):
    about = AboutUs.objects.get()
    return render(request, 'about_us.html', {'about': about})


def menu(request):
    m = Menu.objects.all()
    return render(request, 'menu.html', {'m': m})
