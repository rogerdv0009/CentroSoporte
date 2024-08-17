from django.db import models
from base.models import Modelo_Base
# Create your models here.

class Noticia(Modelo_Base):

    titulo = models.CharField("Título", max_length=50, null=False, blank=False)
    resumen = models.CharField("Resúmen", max_length=150, null=False, blank=False)
    descripcion = models.TextField("Descripción", null=False, blank=False)
    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False, null=False, blank=False)
    imagen = models.ImageField("Imagen", upload_to="noticias/", height_field=None, width_field=None, max_length=None,
                               null=True, blank=True)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-id']

    def __str__(self):
        return self.titulo
