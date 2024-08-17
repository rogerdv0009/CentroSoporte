from django.urls import path
from .views import *

urlpatterns = [
    path("listado/", ProductoListView.as_view(), name="Listado_Producto"),
    path("crear/", ProductoCreateView.as_view(), name="Crear_Producto"),
    path("eliminar/<int:pk>/", ProductoDeleteView.as_view(), name="Eliminar_Producto"),
    path("editar/<int:pk>/", ProductoUpdateView.as_view(), name="Editar_Producto"),
    path("detalle/<int:pk>/", ProductoDetailView.as_view(), name="Detalle_Producto"),
]