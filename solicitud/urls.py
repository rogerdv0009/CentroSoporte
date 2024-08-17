from django.urls import path
from .views import *

urlpatterns = [
    path("", SolicitudView.as_view(), name="Solicitudes"),
    #Cambiar estado aprobado
    path("estado/<int:id_objeto>/", cambiarEstadoAprobado, name="Cambio"),
    path("estado_s/<int:id_objeto>/", cambiarEstadoAprobadoSoporte, name="Cambio_S"),
    #////////////////////////////////////////////////////////////////////////////////////
    #urls Solicitud Servicios
    path("listado/", Solicitud_ServicioListView.as_view(), name="Listado_Solicitud_Servicio"),
    path("crear/", crearSolicitudServicio, name="Crear_Solicitud_Servicio"),
    path("eliminar/<int:pk>/", Solicitud_ServicioDeleteView.as_view(), name="Eliminar_Solicitud_Servicio"),
    path("detalle/<int:pk>/", Solicitud_ServicioDetailView.as_view(), name="Detalle_Solicitud_Servicio"),
    #////////////////////////////////////////////////////////////////////////////////////////
    #urls Solicitud Soporte
    path("listado_s_s/", Solicitud_SoporteListView.as_view(), name="Listado_Solicitud_Soporte"),
    path("crear_s_s/", crearSolicitudSoporte, name="Crear_Solicitud_Soporte"),
    path("eliminar_s_s/<int:pk>/", Solicitud_SoporteDeleteView.as_view(), name="Eliminar_Solicitud_Soporte"),
    path("detalle_s_s/<int:pk>/", Solicitud_SoporteDetailView.as_view(), name="Detalle_Solicitud_Soporte"),
]