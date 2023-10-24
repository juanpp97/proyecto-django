from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RoomType, RoomImg, RoomView
from .forms import RoomForm, RoomViewForm
from django.contrib import messages
from os import path
# Create your views here.

class RoomListView(ListView):
    model = RoomType
    context_object_name = 'rooms_list'
    template_name = 'administracion/listar_hab.html'

def rename_image(image, new_name):
    file_name, file_extension = path.splitext(image.name)
    new_name = f"{new_name}{file_extension}"
    image.name = new_name

class RoomCreateView(CreateView):
    model = RoomType
    form_class = RoomForm
    template_name = 'administracion/form_hab.html'
    success_url = reverse_lazy('listar_hab')
    def form_valid(self, form):
        self.object = form.save()
        if self.request.FILES:
            for indice, imagen in enumerate(self.request.FILES.getlist('imgs')):
                rename_image(imagen, f"{self.object.name}_{indice}")
                RoomImg.objects.create(img = imagen, room = self.object)
        messages.success(self.request, "Habitación guardada con éxito")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error al crear la habitación")
        return super().form_invalid(form)
        
    
class RoomViewCreateView(CreateView):
    model = RoomView
    form_class = RoomViewForm
    template_name = 'administracion/crear_vista.html'
    success_url = reverse_lazy('listar_hab')
    def form_valid(self, form):
        messages.success(self.request, "Vista Añadida con éxito")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error al crear la vista")
        return super().form_invalid(form)
        
    
    