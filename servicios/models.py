from django.db import models
from base.models import Modelo_Base
# Create your models here.
tipo_servicio = {
    ("Online", "Online"),
    ("Especializados", "Especializados"),
    ("Otro", "Otro"),
}
class Servicio(Modelo_Base):

    titulo = models.CharField("Título", max_length=150, null=False, blank=False)
    descripcion = models.TextField("Descripción", null=False, blank=False)
    imagen = models.ImageField("Imagen", upload_to="servicios/", height_field=None, width_field=None, max_length=None, 
                               null=True, blank=True)
    tipo = models.CharField("Tipo", max_length=50, null=False, blank=False, choices=tipo_servicio)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-id']

    def __str__(self):
        return self.titulo

