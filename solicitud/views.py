from django.shortcuts import redirect,HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, TemplateView
from servicios.models import Servicio
from soporte.models import Soporte
from .models import Solicitud_Servicio, Solicitud_Soporte
from .forms import Solicitud_ServicioModelForm, Solicitud_SoporteModelForm

# Create your views here.
# Escoger tipos de Solicitud
class SolicitudView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    login_url = "Login"
    permission_required='solicitud_servicio.view_solicitud_servicio'
    template_name = "solicitudes/solicitud.html"

#Cambiar estado aprobado de solicitud_servicio
#@method_decorator(login_required)
def cambiarEstadoAprobado(request,id_objeto):
    solicitud = Solicitud_Servicio.objects.get(id = id_objeto)
    solicitud.aprobado = True
    solicitud.save()
    return redirect('Listado_Solicitud_Servicio')

#Cambiar estado de solicitud Soporte

def cambiarEstadoAprobadoSoporte(request,id_objeto):
    solicitud = Solicitud_Soporte.objects.get(id = id_objeto)
    solicitud.aprobado = True
    solicitud.save()
    return redirect('Listado_Solicitud_Soporte')

#Crear Solicitud Servicio
def crearSolicitudServicio(request):
    if request.method == 'POST':
        form = Solicitud_ServicioModelForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            descripcion = form.cleaned_data['descripcion']
            id_servicio = request.POST['id_servicio_hidden']
            servicio = Servicio.objects.get(id = id_servicio)
            contador = Solicitud_Servicio.objects.filter(correo=correo, id_servicio=id_servicio).count()
            if contador > 5:
                return HttpResponse('presenta mas de 5 solicitudes a este servicio. Puede estar ocasionando spam en el servidor')
            else:
                solicitud = Solicitud_Servicio(correo = correo, telefono = telefono, descripcion = descripcion, id_servicio = servicio)
                solicitud.save()
                return redirect('Listado_Servicio')
        else:
            return HttpResponse("el formulario no es valido")
    else:
        return HttpResponse('Se esta enviando el formulario incorrectamente')

#Crear Solicitud Soporte
def crearSolicitudSoporte(request):
    if request.method == 'POST':
        form = Solicitud_SoporteModelForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            descripcion = form.cleaned_data['descripcion']
            id_soporte = request.POST['id_servicio_hidden']
            soporte = Soporte.objects.get(id = id_soporte)
            contador = Solicitud_Soporte.objects.filter(correo=correo, id_soporte=id_soporte).count()
            if contador > 5:
                return HttpResponse('presenta mas de 5 solicitudes a este soporte. Puede estar ocasionando spam en el servidor')
            else:
                solicitud = Solicitud_Soporte(correo = correo, telefono = telefono, descripcion = descripcion, id_soporte = soporte)
                solicitud.save()
                return redirect('Listado_Soporte')
        else:
            return HttpResponse("el formulario no es valido")
    else:
        return HttpResponse('Se esta enviando el formulario incorrectamente')


#Solicitudes de Servicio
class Solicitud_ServicioListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    login_url = "Login"
    permission_required='solicitud_servicio.view_solicitud_servicio'
    model = Solicitud_Servicio
    template_name = "solicitudes/servicio/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.GET.get('catalogo')
        if valor_select == 'Sin aprobar':
            queryset = queryset.filter(estado=True, aprobado=False)
        else:
            queryset = queryset.filter(estado=True, aprobado=True)
        return queryset
    
class Solicitud_ServicioDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    login_url = "Login"
    permission_required='solicitud_servicio.delete_solicitud_servicio'
    model = Solicitud_Servicio
    template_name = "solicitudes/servicio/eliminar.html"
    success_url = reverse_lazy("Listado_Solicitud_Servicio")
    
    def post(self, request, pk, *args, **kwargs):
        object = Solicitud_Servicio.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Listado_Solicitud_Servicio')
    
    
class Solicitud_ServicioUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    login_url = "Login"
    permission_required='solicitud_servicio.change_solicitud_servicio'
    model = Solicitud_Servicio
    template_name = "solicitudes/servicio/editar.html"
    form_class = Solicitud_ServicioModelForm
    success_url = reverse_lazy("Listado_Solicitud_Servicio")

class Solicitud_ServicioDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    login_url = "Login"
    permission_required='solicitud_servicio.view_solicitud_servicio'
    model = Solicitud_Servicio
    template_name = "solicitudes/servicio/detalle.html"
    
#////////////////////////////////////////////////////////////////////////////////

#Solicitudes de Soportes

class Solicitud_SoporteListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    login_url = "Login"
    permission_required='solicitud_soporte.view_solicitud_soporte'
    model = Solicitud_Soporte
    template_name = "solicitudes/soporte/listado.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        valor_select = self.request.GET.get('catalogo')
        if valor_select == 'Sin aprobar':
            queryset = queryset.filter(estado=True, aprobado=False)
        else:
            queryset = queryset.filter(estado=True, aprobado=True)
        return queryset
    
class Solicitud_SoporteDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    login_url = "Login"
    permission_required='solicitud_soporte.delete_solicitud_soporte'
    model = Solicitud_Soporte
    template_name = "solicitudes/soporte/eliminar.html"
    success_url = reverse_lazy("Listado_Solicitud_Soporte")
    
    def post(self, request, pk, *args, **kwargs):
        object = Solicitud_Soporte.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('Listado_Solicitud_Soporte')
    
    
class Solicitud_SoporteUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    login_url = "Login"
    permission_required='solicitud_soporte.change_solicitud_soporte'
    model = Solicitud_Soporte
    template_name = "solicitudes/soporte/editar.html"
    form_class = Solicitud_SoporteModelForm
    success_url = reverse_lazy("Listado_Solicitud_Soporte")

class Solicitud_SoporteDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    login_url = "Login"
    permission_required='solicitud_soporte.view_solicitud_soporte'
    model = Solicitud_Soporte
    template_name = "solicitudes/soporte/detalle.html"
    
    