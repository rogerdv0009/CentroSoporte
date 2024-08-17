from django.db import models
from base.models import Modelo_Base


class Producto(Modelo_Base):

    titulo = models.CharField("Título", max_length=150, null=False, blank=False)
    descripcion = models.TextField("Descripción", null=False, blank=False)
    imagen = models.ImageField("Imagen", upload_to="producto/", height_field=None, width_field=None, max_length=None,
                               null=True, blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-id']

    def __str__(self):
        return self.titulo


