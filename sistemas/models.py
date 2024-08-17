from django.db import models
from base.models import Modelo_Base
# Create your models here.

class Sistema(Modelo_Base):

    titulo = models.CharField("Título", max_length=150, null=False, blank=False)
    siglas = models.CharField("Siglas", max_length=10, null=False, blank=False)
    descripcion = models.TextField("Descripción", null=False, blank=False)

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ['-id']

    def __str__(self):
        return self.titulo

