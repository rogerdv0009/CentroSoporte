from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
rol_usuario ={
    ("Especialista", "Especialista"),
    ("Cliente", "Cliente"),
    ("Administrador", "Administrador")
}
class Usuario(AbstractUser):
    rol=models.CharField("Rol", max_length=50, choices=rol_usuario, default="Cliente")