from django.urls import path
from .views import *

urlpatterns = [
    path("login/", LoginFormView.as_view(), name="Login"),
    path("logout/", CerrarSesion.as_view(), name="Logout"),
    path("listado_usuario/", UsuarioListView.as_view(), name="Listado_Usuario"),
    path("crear_usuario/", UsuarioCreateView.as_view(), name="Crear_Usuario"),
    path("eliminar_usuario/<int:pk>/", UsuarioDeleteView.as_view(), name="Eliminar_Usuario"),
    path("editar_usuario/<int:pk>/", UsuarioUpdateView.as_view(), name="Editar_Usuario"),
]