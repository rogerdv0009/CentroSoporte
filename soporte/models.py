from django.db import models
from base.models import Modelo_Base
from servicios.models import Servicio
# Create your models here.

class Soporte(Modelo_Base):

    titulo = models.CharField("Título", max_length=150, null=False, blank=False)
    descripcion = models.TextField("Descripción", null=False, blank=False)
    imagen = models.ImageField("Imagen", upload_to="soporte/", height_field=None, width_field=None, max_length=None,
                               null=True, blank=True)
    servicios = models.ManyToManyField(Servicio, verbose_name="Servicios Asociados")
    
    class Meta:
        verbose_name = "Soporte"
        verbose_name_plural = "Soportes"
        ordering = ['-id']

    def __str__(self):
        return self.titulo

