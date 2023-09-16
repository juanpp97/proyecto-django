from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, "inicio.html", {"ahora": datetime.now()} )

def rooms(request):
    return render(request, 'habitaciones.html')