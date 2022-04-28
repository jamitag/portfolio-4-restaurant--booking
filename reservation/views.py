from django.shortcuts import render
from .models import reservation

def index(request):
    reservations = reservation.objects.all()
    context = {
        'reservations': reservations
    }

    return render(request, 'index.html', context=context)


