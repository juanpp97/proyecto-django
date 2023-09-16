from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        "date": datetime.now(),
        "active": "index",
    }
    return render(request, "reservas/inicio.html", context)

def rooms(request):
    context = {
        "date": datetime.now(),
        "active": "rooms",
    }
    return render(request, 'reservas/habitaciones.html')

def facilities(request):
    context = {
        "date": datetime.now(),
        "active": "rooms",
        "imagenes": [
            {"img":"img/facilities/instalaciones_01.webp","titulo":"example 1"},
            {"img":"img/facilities/instalaciones_02.webp","titulo":"example 2"},
            {"img":"img/facilities/instalaciones_01.webp","titulo":"example 3"},
            {"img":"img/facilities/instalaciones_02.webp","titulo":"example 4"}
            ]
    }
    return render(request, "./facilities/facilities.html", context)
