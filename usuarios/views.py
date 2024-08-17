from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import RedirectView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView

from usuarios.models import Usuario
from usuarios.forms import CrearUsuarioModelForm

#Autenticar
class LoginFormView(LoginView):
    template_name = 'base/login.html'
    success_url = reverse_lazy('Principal')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

#//////////////////////////////////////////////////////////////////////////////////////

#Cerrar Sesion
class CerrarSesion(RedirectView):
    pattern_name = 'Principal'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    
#/////////////////////////////////////////////////////////////////////////////////////

class UsuarioListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    login_url = "Login"
    permission_required='usuario.view_usuario'
    model = Usuario
    template_name = "usuarios/listado.html"
    
class UsuarioDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    login_url = "Login"
    permission_required='usuario.delete_usuario'
    model = Usuario
    template_name = "usuarios/eliminar.html"
    success_url = reverse_lazy("Listado_Usuario")
    
class UsuarioCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    login_url = "Login"
    permission_required='usuario.add_usuario'
    model = Usuario
    template_name = "usuarios/crear.html"
    form_class = CrearUsuarioModelForm
    success_url = reverse_lazy("Listado_Usuario")
    
class UsuarioUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url = "Login"
    permission_required='usuario.change_usuario'
    model = Usuario
    template_name = "usuarios/editar.html"
    form_class = CrearUsuarioModelForm
    success_url = reverse_lazy("Listado_Usuario")
