from django.urls import path
from . import views

urlpatterns = [
    path('inicio/',views.inicio, name= 'inicio'),
    path('habitacion/productos/', views.habitacion, name="productos"),
    path('habitacion/productos/<str:tipo>', views.habitacion, name="serv-producto"),
    # path('habitacion/carrito', views.carrito, name="serv-carrito"),
    path('actividades/', views.actividades, name='actividades'),
    path('json/carrito', views.actividades, name='actividades'),
]