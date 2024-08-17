from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Categoria
from .forms import CategoriaModelForm

# Create your views here.
class CategoriaListView(ListView):
    model = Categoria
    template_name = "categoria/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=True)
        return queryset
    
class CategoriaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url = "Login"
    permission_required = 'categoria.delete_categoria'
    model = Categoria
    template_name = "categoria/eliminar.html"
    success_url = reverse_lazy("Listado_Categoria")
    
    def post(self, request, pk, *args, **kwargs):
        object = Categoria.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Listado_Categoria')
    
class CategoriaCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    login_url = "Login"
    permission_required = 'categoria.add_categoria'
    model = Categoria
    template_name = "categoria/crear.html"
    form_class = CategoriaModelForm
    success_url = reverse_lazy("Listado_Categoria")
    
class CategoriaUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url = "Login"
    permission_required = 'categoria.change_categoria'
    model = Categoria
    template_name = "categoria/editar.html"
    form_class = CategoriaModelForm
    success_url = reverse_lazy("Listado_Categoria")

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = "categoria/detalle.html"
    
    