from django.urls import path
from .views import *

urlpatterns = [
    path("listado/", CategoriaListView.as_view(), name="Listado_Categoria"),
    path("crear/", CategoriaCreateView.as_view(), name="Crear_Categoria"),
    path("eliminar/<int:pk>/", CategoriaDeleteView.as_view(), name="Eliminar_Categoria"),
    path("editar/<int:pk>/", CategoriaUpdateView.as_view(), name="Editar_Categoria"),
    path("detalle/<int:pk>/", CategoriaDetailView.as_view(), name="Detalle_Categoria"),
]