from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('reservation/', views.create_reservation, name = 'reservation'),
    path('update-reservation/<str:pk>/', views.updateReservation, name = 'updateReservation'),
    path('delete-reservation/<str:pk>/', views.deleteReservation, name = 'deleteReservation'),
    path('reservations/', views.Reservations, name = 'Reservations')
]