from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('habitaciones/', views.rooms, name="rooms"),
    path('reserva/<int:id_hab>', views.reservation, name='reservation'),

    path('instalaciones/', views.facilities, name='facilities'),
    path('contacto/', views.contact, name='contact'),
]
