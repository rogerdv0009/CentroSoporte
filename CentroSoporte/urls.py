"""
URL configuration for CentroSoporte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from django.urls import path, re_path, include

from CentroSoporte.settings import MEDIA_ROOT
from base.views import HomeTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeTemplateView.as_view(), name="Principal"),
    path("noticias/", include('noticias.urls')),
    path("categorias/", include('categoria.urls')),
    path("productos/", include('producto.urls')),
    path("servicios/", include('servicios.urls')),
    path("servicios/", include('servicios.urls')),
    path("solicitudes/", include('solicitud.urls')),
    path("soportes/", include('soporte.urls')),
    path("usuarios/", include('usuarios.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': MEDIA_ROOT,
    })
]