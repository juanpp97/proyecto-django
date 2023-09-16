from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, "inicio.html", {"ahora": datetime.now()} )

def rooms(request):
    return render(request, 'habitaciones.html')

def facilities(request):
    context = {
        "imagenes": [
            {"img":"img/facilities/instalaciones_01.webp","titulo":"example 1"},
            {"img":"img/facilities/instalaciones_02.webp","titulo":"example 2"},
            {"img":"img/facilities/instalaciones_01.webp","titulo":"example 3"},
            {"img":"img/facilities/instalaciones_02.webp","titulo":"example 4"}
            ]
    }
    return render(request, "./facilities/facilities.html", context)
