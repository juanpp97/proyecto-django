from django.shortcuts import render
from .models import Eventos
# Create your views here.

def servicios_adicionales (request):
    return render (request, 'servicios/servicios_adic.html')



def actividades(request):
    model = Eventos
    contexto = {
        "list_eventos": model.objects.all()
    }
    return render (request, 'servicios/actividades.html',contexto)