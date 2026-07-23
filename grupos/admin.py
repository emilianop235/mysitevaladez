from django.contrib import admin
from .models import grupos


class GruposAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estatus', 'fecha_creacion')
    ordering = ('nombre',)
admin.site.register(grupos, GruposAdmin)
