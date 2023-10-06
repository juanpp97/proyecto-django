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