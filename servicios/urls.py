from django.urls import path
from . import views

urlpatterns = [
    path('habitacion/productos/', views.habitacion, name="serv_index"),
    path('habitacion/productos/<str:tipo>', views.habitacion, name="serv-producto"),
    # path('habitacion/carrito', views.carrito, name="serv-carrito"),
    path('actividades/', views.actividades, name='actividades'),
    
    
]