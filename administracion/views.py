from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import RoomType, RoomImg, RoomView, Price
from .forms import RoomForm, RoomViewForm, PriceForm
from django.contrib import messages
from os import path, rename
from datetime import datetime
# Create your views here.

class RoomListView(PermissionRequiredMixin, ListView):
    model = RoomType
    context_object_name = 'rooms_list'
    login_url = 'accounts-hanfler'
    permission_required = 'administracion.view_roomtype'
    template_name = 'administracion/listar_hab.html'
    ordering = ['capacity']
    def handle_no_permission(self):
        messages.error(self.request, "No tenes permisos flaco")
        return redirect(reverse_lazy('index'))
    def get(self, request, *args, **kwargs):
        if 'ordering' in request.GET:
            print(request.GET["ordering"])
            self.ordering = [request.GET["ordering"]]
        return super().get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = datetime.now()
        return context
    
def rename_image(image, new_name):
    file_name, file_extension = path.splitext(image.name)
    new_name = f"{new_name}{file_extension}"
    image.name = new_name

class RoomCreateView(LoginRequiredMixin, CreateView):
    login_url = 'accounts-hanfler'
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
        context["titulo"] = "Nuevo Tipo de Habitación"
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
                        image.delete()

            orig_room = RoomType.objects.get(pk = self.object.pk)
            exist_imgs = RoomImg.objects.filter(room = orig_room)
            #Si cambio el nombre del producto cambio los nombres de las imagenes almacenadas
            if orig_room.name != room.name:
                for index, imagen in enumerate(exist_imgs):
                    try:
                        nuevo_nombre = f"habitaciones/{room.name.replace(' ', '_')}_{index}"
                        old_path = imagen.img.path
                        rename_image(imagen.img, nuevo_nombre)             
                        rename(old_path, imagen.img.path)
                        imagen = imagen.save()
                    except Exception as e:
                        return self.form_invalid(form)

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
            return self.form_invalid(form)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error al modificar los datos")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar Tipo de Habitación"
        context["date"] = datetime.now()
        context["boton"] = "Editar"
        return context
    
        
class RoomDeleteView(DeleteView):
    model = RoomType
    template_name = 'administracion/eliminar.html'
    success_url = reverse_lazy('listar_hab')
    context_object_name = 'room'

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = datetime.now()
        return context
    

class RoomViewCreateView(CreateView):
    model = RoomView
    form_class = RoomViewForm
    template_name = 'administracion/form.html'
    success_url = reverse_lazy('listar_vista')
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
        context["boton"] = "Crear"
        context["url"] = reverse_lazy('listar_vista')

        return context

class RoomViewUpdateView(UpdateView):
    model = RoomView
    form_class = RoomViewForm
    template_name = 'administracion/form.html'
    success_url = reverse_lazy('listar_vista')
    def form_valid(self, form):
        messages.success(self.request, 'La vista se ha actualizado correctamente')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar la vista')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar Vista"
        context["date"] = datetime.now()
        context["boton"] = "Editar"
        context["url"] = reverse_lazy('listar_vista')
        return context
    
    
class RoomViewDeleteView(DeleteView):
    model = RoomView
    template_name = 'administracion/eliminar.html'
    success_url = reverse_lazy('listar_vista')
    def form_valid(self, form):
        messages.success(self.request, 'La vista se ha borrado correctamente')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al borrar la vista')
        return super().form_invalid(form) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = datetime.now()
        context["titulo"] = "Eliminar Vista"
        context["url"] = reverse_lazy("listar_vista")
        context["aviso"] = f"¿Está seguro que desea eliminar permanentemente la vista {self.object.name}?"
        return context
    
    
    

class PriceCreateView(CreateView):
    model = Price
    form_class = PriceForm
    template_name = 'administracion/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Tarifa guardada con éxito")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Ha ocurrido un error al crear la tarifa")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Nueva Tarifa"
        context["boton"] = "Crear"
        context["url"] = reverse_lazy("index")
        context["date"] = datetime.now()
        return context
    
