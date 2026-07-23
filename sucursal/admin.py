from django.contrib import admin
from .models import sucursal

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono', 'encargado')
    list_filter = ('estatus',)
    ordering = ('nombre',)
admin.site.register(sucursal, SucursalAdmin)
