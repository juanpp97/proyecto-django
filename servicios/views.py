from django.shortcuts import render
from .models import Eventos,Producto

# Create your views here.

def servicios_adicionales (request):

    listado = list(Producto.objects.all())

   


    return render (request, 'servicios/servicios_adic.html', {'lista': listado} )



def actividades(request):
    model = Eventos
    contexto = {
        "list_eventos": model.objects.all()
    }
    return render (request, 'servicios/actividades.html',contexto)