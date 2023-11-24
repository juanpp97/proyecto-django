from typing import Any
from django.db import models
from django.db.models.query import QuerySet

# Create your models here.

class RoomView(models.Model):
    name = models.CharField(verbose_name="Vista")
    def __str__(self) -> str:
        return f"{self.name}"

class RoomType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la habitación')
    capacity = models.IntegerField(verbose_name='Capacidad Máxima')
    view = models.ManyToManyField(RoomView, verbose_name="Vista")
    num_beds = models.CharField(verbose_name="Número de camas")

    def display_view(self):
        return ', '.join([romview.name for romview in self.view.all()])

    def __str__(self) -> str:
        return f"{self.name} - {self.capacity} - {self.num_beds}"
    

class RoomImg(models.Model):
    img = models.ImageField(upload_to="habitaciones/", verbose_name="Imagen de la habitacion", null=True)
    room = models.ForeignKey(RoomType,on_delete=models.CASCADE, related_name="room_imgs")
    
    def __str__(self) -> str:
        return f"{self.img}"
    
    def delete(self, using=None, keep_parents=False):
        self.img.storage.delete(self.img.name)
        super().delete()


class Price(models.Model):
    date_from = models.DateField(verbose_name="Desde: ")
    date_to = models.DateField(verbose_name="Hasta: ")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor por noche (AR$)", help_text="Usar punto (.) para los decimales y no usar separador de miles")
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name="Tipo de Habitación", related_name="type")
    room_view = models.ForeignKey(RoomView, on_delete=models.CASCADE, verbose_name="Vista de la Habitación")
    def __str__(self):
        return f"{self.room_type.name} ({self.room_view.name}): {self.date_from} a {self.date_to}: AR${self.price}"



class Room(models.Model):
    class EstadoChoices(models.TextChoices):
        ACTIVO = 'A', 'Activo'
        INACTIVO = 'I', 'Inactivo'
        MANTENIMIENTO = 'M', 'En Mantenimiento'
    number = models.CharField(max_length=10, verbose_name="Número de habitación")
    status = models.CharField(max_length=1, choices=EstadoChoices.choices, verbose_name="Estado")
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='room_type')
    view = models.ForeignKey(RoomView, on_delete=models.CASCADE, related_name='room_view')

    