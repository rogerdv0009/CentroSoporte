from django.urls import path
from .views import *

urlpatterns = [
    path("listado/", SistemaListView.as_view(), name="Listado_Sistema"),
    path("crear/", SistemaCreateView.as_view(), name="Crear_Sistema"),
    path("eliminar/<int:pk>/", SistemaDeleteView.as_view(), name="Eliminar_Sistema"),
    path("editar/<int:pk>/", SistemaUpdateView.as_view(), name="Editar_Sistema"),
    path("detalle/<int:pk>/", SistemaDetailView.as_view(), name="Detalle_Sistema"),
]