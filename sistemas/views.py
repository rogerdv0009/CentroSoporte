from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Sistema
from .forms import SistemaModelForm

# Create your views here.
class SistemaListView(ListView):
    model = Sistema
    template_name = "sistemas/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=True)
        return queryset
    
class SistemaDeleteView(DeleteView):
    model = Sistema
    template_name = "sistemas/eliminar.html"
    success_url = reverse_lazy("Listado_Sistema")
    
    def post(self, request, pk, *args, **kwargs):
        object = Sistema.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Listado_Sistema')
    
class SistemaCreateView(CreateView):
    model = Sistema
    template_name = "sistemas/crear.html"
    form_class = SistemaModelForm
    success_url = reverse_lazy("Listado_Sistema")
    
class SistemaUpdateView(UpdateView):
    model = Sistema
    template_name = "sistemas/editar.html"
    form_class = SistemaModelForm
    success_url = reverse_lazy("Listado_Sistema")

class SistemaDetailView(DetailView):
    model = Sistema
    template_name = "sistemas/detalle.html"
