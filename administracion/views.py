<<<<<<< HEAD
=======
from typing import Any
from django.http import HttpRequest, HttpResponse
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RoomType, RoomImg, RoomView
from .forms import RoomForm, RoomViewForm
from django.contrib import messages
from os import path, remove, rename
from datetime import datetime, timedelta
# Create your views here.

class RoomListView(ListView):
    model = RoomType
    context_object_name = 'rooms_list'
    template_name = 'administracion/listar_hab.html'
    ordering = ['capacity']
<<<<<<< HEAD
=======
    def get(self, request, *args, **kwargs):
        if 'ordering' in request.GET:
            print(request.GET["ordering"])
            self.ordering = [request.GET["ordering"]]
        return super().get(request, *args, **kwargs)
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = datetime.now()
        return context
    
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
            for index, image in enumerate(self.request.FILES.getlist('imgs')):
                rename_image(image, f"{self.object.name}_{index}")
                RoomImg.objects.create(img = image, room = self.object)
        messages.success(self.request, "Habitación guardada con éxito")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error al crear la habitación")
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
<<<<<<< HEAD
        context["titulo"] = "Crear Nueva Habitación"
=======
        context["titulo"] = "Nuevo Tipo de Habitación"
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
        context["boton"] = "Crear"
        
        context["date"] = datetime.now()
        return context
    


class RoomUpdateView(UpdateView):
    model = RoomType
    form_class = RoomForm
    template_name = 'administracion/form_hab.html'
    success_url = reverse_lazy('listar_hab')

    def form_valid(self, form):
        room = form.save(commit=False)
        try:
            #Si está presente el campo imagenes para borrar
            if 'imgs_delete' in form.fields:
                borrar_imgs = form.cleaned_data['imgs_delete']
                if borrar_imgs:        
                    for image in borrar_imgs:
<<<<<<< HEAD
                        if path.exists(image.img.path):
                            remove(image.img.path)
=======
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
                        image.delete()

            orig_room = RoomType.objects.get(pk = self.object.pk)
            exist_imgs = RoomImg.objects.filter(room = orig_room)
            #Si cambio el nombre del producto cambio los nombres de las imagenes almacenadas
            if orig_room.name != room.name:
                for index, imagen in enumerate(exist_imgs):
<<<<<<< HEAD
                    ruta = imagen.img.name.split("/")
                    nombre = ruta.pop()
                    nombre, extension = path.splitext(nombre)
                    nuevo_nombre = f"{room.name.replace(' ', '_')}_{index}" + extension
                    ruta.append(nuevo_nombre)
                    path_ant = imagen.img.path
                    imagen.img.name =  "/".join(ruta)
                    rename(path_ant, imagen.ruta.path)
                    imagen.save()
=======
                    try:
                        nuevo_nombre = f"habitaciones/{room.name.replace(' ', '_')}_{index}"
                        old_path = imagen.img.path
                        rename_image(imagen.img, nuevo_nombre)             
                        rename(old_path, imagen.img.path)
                        imagen = imagen.save()
                    except Exception as e:
                        return self.form_invalid(form)
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b

            if self.request.FILES.getlist('imgs'):
                indice_max = 0
                for imagen in exist_imgs:
                    nombre, extension = path.splitext(imagen.img.name)
                    if "_" in nombre:
                        if int(nombre.split("_")[-1]) > indice_max:
                            indice_max = int(nombre.split("_")[-1])
                index = indice_max
                for image in self.request.FILES.getlist('imgs'):
                    index += 1
                    rename_image(image, f"{self.object.name}_{index}")
                    RoomImg.objects.create(room = self.object , img = image )
            room.save()
            messages.success(self.request, "Los datos se han modificado correctamente")
        except BaseException as e:
<<<<<<< HEAD
            messages.error(self.request, "Ha ocurrido un error")
=======
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
            return self.form_invalid(form)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error al modificar los datos")
        return super().form_invalid(form)
<<<<<<< HEAD
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar Habitación"
=======

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar Tipo de Habitación"
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
        context["date"] = datetime.now()
        context["boton"] = "Editar"
        return context
    
        
class RoomDeleteView(DeleteView):
    model = RoomType
    template_name = 'administracion/eliminar.html'
    success_url = reverse_lazy('listar_hab')
    context_object_name = 'room'
<<<<<<< HEAD
    def form_valid(self, form):
        if RoomImg.objects.filter(room = self.object).exists():
            for image in RoomImg.objects.filter(room = self.object):
                if path.exists(image.img.path):
                    remove(image.img.path)
        return super().form_valid(form)
    
=======

    def form_valid(self, form):
        try:
            if RoomImg.objects.filter(room = self.object).exists():
                for image in RoomImg.objects.filter(room = self.object):
                    image.delete()
        except Exception as e:
            return self.form_invalid(form)
        messages.success(self.request, "Habitación eliminada correctamente")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al borrar la habitación")
        return super().form_invalid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = datetime.now()
        context["titulo"] = "Eliminar Habitación"
        context["url"] = reverse_lazy("listar_hab")
        context["aviso"] = f"¿Está seguro que desea eliminar permanentemente la {self.object.name}?"
        return context
    

class RoomViewListView(ListView):
    model = RoomView
    template_name = 'administracion/listar_vistas.html'
    context_object_name = 'views_list'
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = datetime.now()
        return context
    

class RoomViewCreateView(CreateView):
    model = RoomView
    form_class = RoomViewForm
<<<<<<< HEAD
    template_name = 'administracion/crear_vista.html'
    success_url = reverse_lazy('listar_hab')
=======
    template_name = 'administracion/form_vista.html'
    success_url = reverse_lazy('listar_vista')
>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
    def form_valid(self, form):
        messages.success(self.request, "Vista Añadida con éxito")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error al crear la vista")
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Crear Vista de Habitación"
        context["date"] = datetime.now()

        return context
<<<<<<< HEAD
    
=======



>>>>>>> a1529cbcdd7469fa57e868ff8062cfbd74b2a22b
        
        
    

