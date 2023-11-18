from typing import Any
from django.db import models

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
    def __str__(self) -> str:
        return f"{self.name} - {self.capacity} - {self.view} - {self.num_beds}"
    

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
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name="Tipo de Habitación")
   
    def __str__(self):
        return f"{self.date_from} a {self.date_to}: AR${self.price}"