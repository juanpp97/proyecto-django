from django.db import models
from django.utils import timezone
# Create your models here.
class Eventos(models.Model):
    titulo = models.CharField(verbose_name='Titulo', max_length=44, null=False, blank=False)
    informacion = models.CharField(verbose_name='Informacion',max_length=244, null=False, blank=True)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='eventos/')
    lugar = models.CharField(verbose_name='Lugar',max_length=144, null=True, blank=True, default='Preguntar')
    fecha = models.DateField(default=timezone.now)
    # contenido = models.JSONField()

    def __str__(self) -> str:
        return self.titulo
    

class Producto(models.Model):
    opciones_categoria = [('comidas','comidas'),('cafeteria','cafeteria' ),('bebidas','bebidas')]
    nombre = models.CharField(verbose_name="nombre", max_length=100 , null= False, blank=False)
    categoria = models.CharField(verbose_name="categoria", max_length=100 , null= False, blank=False , choices= opciones_categoria)
    precio = models.IntegerField(verbose_name="precio", null= False, blank=False)
    imagen = models.ImageField(verbose_name= "imagen", upload_to="productos/")

    def __str__(self):
        return f"{self.nombre}, {self.categoria},{self.precio}"
