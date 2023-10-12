from django.db import models
from django.utils import timezone
# Create your models here.
class Eventos(models.Model):
    titulo = models.CharField(verbose_name='Titulo', max_length=44, null=False, blank=False)
    informacion = models.CharField(verbose_name='Informacion',max_length=144, null=False, blank=True)
    imagen = models.URLField(verbose_name='Imagen', default='https://placehold.co/600x400/webp')
    lugar = models.CharField(verbose_name='Lugar',max_length=44, null=True, blank=True, default='Preguntar')
    fecha = models.DateField(default=timezone.now)
    # contenido = models.JSONField()

    def __str__(self) -> str:
        return self.titulo
    

class Producto(models.Model):

    opciones_categoria = [('Platos de Autor','Platos de Autor'),('Opciones rapidas','Opciones rapidas'),('Cocteles y tragos','Cocteles y tragos'),('Whiskeys','Whiskeys'),('Cofee','Cofee'),('Non Cofee','Non Cofee'), ('Smoothie','Smoothie'),('Bakery and pastry','Bakery and pastry')]

    nombre = models.CharField(verbose_name="nombre", max_length=100 , null= False, blank=False)
    categoria = models.CharField(verbose_name="categoria", max_length=100 , null= False, blank=False , choices= opciones_categoria)
    precio = models.IntegerField(verbose_name="precio", max_length=100 , null= False, blank=False)
   

    def __str__(self):
        return f"{self.nombre}, {self.categoria},{self.precio}"
