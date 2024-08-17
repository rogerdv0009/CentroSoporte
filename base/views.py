from django.views.generic import TemplateView
from soporte.models import Soporte
from servicios.models import Servicio
from producto.models import Producto
from noticias.models import Noticia
from categoria.models import Categoria
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def obtenerSoportes(self):
        cont = Soporte.objects.filter(estado=True).count()
        soportes = None
        if cont > 2:
            soportes = Soporte.objects.filter(estado=True)[:3]
        return soportes
    
    def obtenerServicios(self):
        cont = Servicio.objects.filter(estado=True).count()
        soportes = None
        if cont > 3:
            soportes = Servicio.objects.filter(estado=True)[:4]
        return soportes
    
    def obtenerNoticias(self):
        cont = Noticia.objects.filter(estado=True).count()
        soportes = None
        if cont > 2:
            soportes = Noticia.objects.filter(estado=True)[:3]
        return soportes
    
    def obtenerCategorias(self):
        cont = Categoria.objects.filter(estado=True).count()
        soportes = None
        if cont > 4:
            soportes = Noticia.objects.filter(estado=True)[:5]
        return soportes
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["soportes"] = self.obtenerSoportes() 
        context["servicios"] = self.obtenerServicios()
        context["productos"] = Producto.objects.filter(estado=True)
        context["noticias"] = self.obtenerNoticias()
        context["categorias"] = Categoria.objects.filter(estado=True)
        return context
    