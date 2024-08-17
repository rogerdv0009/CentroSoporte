from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Producto
from .forms import ProductoModelForm

# Create your views here.
class ProductoListView(ListView):
    model = Producto
    template_name = "productos/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=True)
        return queryset
    
class ProductoDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    login_url = "Login"
    permission_required='producto.delete_producto'
    model = Producto
    template_name = "productos/eliminar.html"
    success_url = reverse_lazy("Listado_Producto")
    
    def post(self, request, pk, *args, **kwargs):
        object = Producto.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Listado_Producto')
    
class ProductoCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    login_url = "Login"
    permission_required='producto.add_producto'
    model = Producto
    template_name = "productos/crear.html"
    form_class = ProductoModelForm
    success_url = reverse_lazy("Listado_Producto")
    
class ProductoUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url = "Login"
    permission_required='producto.change_producto'
    model = Producto
    template_name = "productos/editar.html"
    form_class = ProductoModelForm
    success_url = reverse_lazy("Listado_Producto")

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/detalle.html"