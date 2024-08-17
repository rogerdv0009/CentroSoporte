from django.urls import path
from .views import *

urlpatterns = [
    #urls Solicitud Servicios
    path("listado/", SoporteListView.as_view(), name="Listado_Soporte"),
    path("crear/", SoporteCreateView.as_view(), name="Crear_Soporte"),
    path("eliminar/<int:pk>/", SoporteDeleteView.as_view(), name="Eliminar_Soporte"),
    path("editar/<int:pk>/", SoporteUpdateView.as_view(), name="Editar_Soporte"),
    path("detalle/<int:pk>/", SoporteDetailView.as_view(), name="Detalle_Soporte"),
]