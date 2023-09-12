from django.urls import path
from . import views

urlpatterns = [
    path('reservas/', views.index, name='index'),
    path('instalaciones/', views.facilities, name='facilities')
]
