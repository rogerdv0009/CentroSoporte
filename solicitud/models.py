from django.db import models
from base.models import Modelo_Base
from servicios.models import Servicio
from soporte.models import Soporte
# Create your models here.

class Solicitud(Modelo_Base):

    correo = models.EmailField("Correo", max_length=254, null=False, blank=False)
    telefono = models.PositiveSmallIntegerField("Teléfono", null=False, blank=False)
    descripcion = models.TextField("Descripción")
    aprobado = models.BooleanField("Aprobado", default=False, null=False, blank=False)

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"
        abstract = True
        

class Solicitud_Servicio(Solicitud):

    id_servicio = models.ForeignKey(Servicio, verbose_name="Servicio", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Solicitud_Servicio"
        verbose_name_plural = "Solicitud_Servicios"
        ordering = ['-id']

    def __str__(self):
        return f'Solicitud {self.id}'


class Solicitud_Soporte(Solicitud):

    id_soporte = models.ForeignKey(Soporte, verbose_name="Plan Soporte", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Solicitud_Soporte"
        verbose_name_plural = "Solicitud_Soportes"
        ordering = ['-id']

    def __str__(self):
        return f'Solicitud {self.id}'



