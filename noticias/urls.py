from django.urls import path
from .views import *

urlpatterns = [
    path("listado/", NoticiaListView.as_view(), name="Listado_Noticia"),
    path("crear/", NoticiaCreateView.as_view(), name="Crear_Noticia"),
    path("eliminar/<int:pk>/", NoticiaDeleteView.as_view(), name="Eliminar_Noticia"),
    path("editar/<int:pk>/", NoticiaUpdateView.as_view(), name="Editar_Noticia"),
    path("detalle/<int:pk>/", NoticiaDetailView.as_view(), name="Detalle_Noticia"),
]