from django.urls import path, include
from reservas import views

urlpatterns = [
    path('reservas/', include('reservas.urls'))
]
