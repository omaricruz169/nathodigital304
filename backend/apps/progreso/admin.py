from django.contrib import admin
from .models import Progreso


@admin.register(Progreso)
class ProgresoAdmin(admin.ModelAdmin):
    list_display = (
        'usuarios',  # <-- Corregido de 'usuario' a 'usuarios' (en plural)
        'juego',
        'nivel',
        'completado',
        'estrellas',
        'mejor_puntaje',
        'veces_jugado',
        'actualizado',
    )
    list_filter = (
        'juego',
        'nivel',
        'completado',
    )
    search_fields = (
        'usuarios__username',
        'usuarios__first_name',
    )