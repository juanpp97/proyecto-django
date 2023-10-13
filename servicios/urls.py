from django.urls import path
from . import views

urlpatterns = [
    path('gestor_servicios/', views.servicios_adicionales, name="serv-adicionales"),
    path('actividades/', views.actividades, name='actividades'),
    
    
]