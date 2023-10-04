from django.urls import path, include

urlpatterns = [
    path('', include('reservas.urls')),
    path('servicios/', include('servicios.urls')),
]
