from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "inicio.html")

def facilities(request):
    context = {
        "imagenes": [
            {"img":"img/facilities/instalaciones_01.webp","titulo":"example 1"},
            {"img":"img/facilities/instalaciones_02.webp","titulo":"example 2"},
            {"img":"img/facilities/instalaciones_01.webp","titulo":"example 3"},
            {"img":"img/facilities/instalaciones_02.webp","titulo":"example 4"}
            ]
    }

    # return HttpResponse(context)
    return render(request, "./facilities/facilities.html", context)