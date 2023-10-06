from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservas.urls')),
    path('servicios/', include('servicios.urls')),
]
