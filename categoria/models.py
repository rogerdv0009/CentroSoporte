from django.db import models
from base.models import Modelo_Base
from sistemas.models import Sistema
# Create your models here.

class Categoria(Modelo_Base):

    titulo = models.CharField("Título", max_length=150, null=False, blank=False)
    imagen = models.ImageField("Imagen", upload_to="categorías/", height_field=None, width_field=None, max_length=None,
                               null=True, blank=True)
    sistemas = models.ManyToManyField(Sistema, verbose_name="Sistemas", blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-id']

    def __str__(self):
        return self.titulo

