from django.urls import path
from .views import *

urlpatterns = [
    path("listado/", ServicioListView.as_view(), name="Listado_Servicio"),
    path("crear/", ServicioCreateView.as_view(), name="Crear_Servicio"),
    path("eliminar/<int:pk>/", ServicioDeleteView.as_view(), name="Eliminar_Servicio"),
    path("editar/<int:pk>/", ServicioUpdateView.as_view(), name="Editar_Servicio"),
    path("detalle/<int:pk>/", ServicioDetailView.as_view(), name="Detalle_Servicio"),
]