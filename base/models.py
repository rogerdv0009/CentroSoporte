from django.db import models

# Create your models here.

class Modelo_Base(models.Model):

    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creado = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    fecha_modificado = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Modelo_Base"
        verbose_name_plural = "Modelo_Bases"
        abstract = True
