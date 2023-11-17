from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('habitaciones/', views.rooms, name="rooms"),
    path('reserva/<int:id_hab>', views.reservation, name='reservation'),
    path('instalaciones/', views.facilities, name='facilities'),
    path('contacto/', views.contact, name='contact'),
    path('accounts/', views.Login_RegistrationView.as_view(), name='accounts_handler'),
    path('logout/', LogoutView.as_view(), name="logout")
    
]
