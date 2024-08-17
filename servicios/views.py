from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from solicitud.forms import Solicitud_ServicioModelForm
from .models import Servicio
from .forms import ServicioModelForm


# Create your views here.
class ServicioListView(ListView):
    model = Servicio
    template_name = "servicios/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=True)
        return queryset
    
class ServicioDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    login_url = "Login"
    permission_required='servicio.delete_servicio'
    model = Servicio
    template_name = "servicios/eliminar.html"
    success_url = reverse_lazy("Listado_Servicio")
    
    def post(self, request, pk, *args, **kwargs):
        object = Servicio.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Listado_Servicio')
    
class ServicioCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    login_url = "Login"
    permission_required='servicio.add_servicio'
    model = Servicio
    template_name = "servicios/crear.html"
    form_class = ServicioModelForm
    success_url = reverse_lazy("Listado_Servicio")
    
class ServicioUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url = "Login"
    permission_required='servicio.change_servicio'
    model = Servicio
    template_name = "servicios/editar.html"
    form_class = ServicioModelForm
    success_url = reverse_lazy("Listado_Servicio")

class ServicioDetailView(DetailView):
    model = Servicio
    template_name = "servicios/detalle.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = Solicitud_ServicioModelForm
        return context
    