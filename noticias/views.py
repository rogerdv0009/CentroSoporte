from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Noticia
from .forms import NoticiaModelForm

# Create your views here.
class NoticiaListView(ListView):
    model = Noticia
    template_name = "noticias/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=True)
        return queryset
    
class NoticiaDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    login_url = "Login"
    permission_required='noticia.delete_noticia'
    model = Noticia
    template_name = "noticias/eliminar.html"
    success_url = reverse_lazy("Listado_Noticia")
    
    def post(self, request, pk, *args, **kwargs):
        object = Noticia.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Listado_Noticia')
    
class NoticiaCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    login_url = "Login"
    permission_required='noticia.add_noticia'
    model = Noticia
    template_name = "noticias/crear.html"
    form_class = NoticiaModelForm
    success_url = reverse_lazy("Listado_Noticia")
    
class NoticiaUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url = "Login"
    permission_required='noticia.change_noticia'
    model = Noticia
    template_name = "noticias/editar.html"
    form_class = NoticiaModelForm
    success_url = reverse_lazy("Listado_Noticia")

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = "noticias/detalle.html"
