
"""
URL configuration for config project.

Rutas principales del backend:
    /admin/         -> Panel de administración de Django
    /api/auth/      -> Registro, login, logout y datos del jugador
    /api/progreso/  -> Avance y progreso en los juegos
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('admin/', admin.site.urls),


    path('api/auth/', include('apps.usuario.urls')),


    path('api/progreso/', include('apps.progreso.urls')),
]
