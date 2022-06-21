from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('about_us/', views.aboutUs, name='aboutUs'),
    path('reservation/', views.create_reservation, name='reservation'),
    path('update-reservation/<str:pk>/', views.updateReservation,
         name='updateReservation'),
    path('delete-reservation/<str:pk>/', views.deleteReservation,
         name='deleteReservation'),
    path('reservations/', views.Reservations, name='Reservations'),
    path('reservations/<str:pk>/', views.Reservations,
         name='ReservationsSuccess'),
]