from django.shortcuts import render

# Create your views here.

def servicios_adicionales (request):
    contexto = {}
    return render (request, 'servicios/servicios_adic.html',contexto)



def instalaciones_adicionales(request):

    return render (request, 'servicios/instalaciones_adic.html')