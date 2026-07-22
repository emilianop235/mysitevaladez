from django.contrib import admin
from .models import sucursal

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'telefono')
admin.site.register(sucursal, SucursalAdmin)