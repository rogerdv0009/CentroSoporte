from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from solicitud.forms import Solicitud_SoporteModelForm
from .models import Soporte
from .forms import SoporteModelForm

# Create your views here.

#Solicitudes de Servicio
class SoporteListView(ListView):
    model = Soporte
    template_name = "soporte/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=True)
        return queryset
    
class SoporteDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    login_url = "Login"
    permission_required='soporte.delete_soporte'
    model = Soporte
    template_name = "soporte/eliminar.html"
    success_url = reverse_lazy("Listado_Soporte")
    
    def post(self, request, pk, *args, **kwargs):
        object = Soporte.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Listado_Soporte')
    
class SoporteCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    login_url = "Login"
    permission_required='soporte.add_soporte'
    model = Soporte
    template_name = "soporte/crear.html"
    form_class = SoporteModelForm
    success_url = reverse_lazy("Listado_Soporte")
    
class SoporteUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url = "Login"
    permission_required='soporte.change_soporte'
    model = Soporte
    template_name = "soporte/editar.html"
    form_class = SoporteModelForm
    success_url = reverse_lazy("Listado_Soporte")

class SoporteDetailView(DetailView):
    model = Soporte
    template_name = "soporte/detalle.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = Solicitud_SoporteModelForm
        return context