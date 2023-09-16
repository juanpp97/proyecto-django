from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('habitaciones/', views.rooms),
    path('instalaciones/', views.facilities, name='facilities'),
]
