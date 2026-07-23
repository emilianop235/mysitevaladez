from django.contrib import admin
from .models import proveedores

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'telefono', 'estatus')
    search_fields = ('nombre', 'apellido', 'direccion', 'telefono')
    list_filter = ('estatus',)
    ordering = ('nombre', 'apellido')

admin.site.register(proveedores, ProveedoresAdmin)
