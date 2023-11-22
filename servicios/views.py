from django.shortcuts import render , redirect
from .models import Eventos,Producto
from datetime import datetime

# Create your views here.

def habitacion (request, tipo="comidas"):
    categorias_disponibles = Producto.objects.values_list('categoria', flat=True).distinct()
    contexto ={"tipo":tipo,}
    if tipo in categorias_disponibles:
        list_productos = Producto.objects.filter(categoria= tipo)
        contexto ={
            "tipo":tipo,
            "list_productos":list_productos
        }
        return render(request,'servicios/habitacion/lista_productos.html',contexto)
    elif tipo == 'carrito':
        return render(request,'servicios/habitacion/carrito.html',contexto)
    else:
        return render(request,'servicios/habitacion/carrito.html',contexto)
    


def actividades(request):
    model = Eventos
    contexto = {
        "list_eventos": model.objects.all()
    }
    return render (request, 'servicios/actividades.html',contexto)


def inicio(request):
    context = {
            "date": datetime.now(),}

    return render (request,'servicios/servicios_adic.html',context)