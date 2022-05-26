from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('reservation/', views.create_reservation, name = 'reservation'),
]