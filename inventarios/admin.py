from django.contrib import admin
from .models import inventarios


class InventariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto_relacionado', 'cantidad', 'ubicacion')
    search_fields = ('nombre', 'descripcion', 'ubicacion', 'producto_relacionado__nombre')
    list_filter = ('estatus', 'ubicacion', 'sucursal', 'proveedor', 'fecha_income')
    ordering = ('-fecha_income',)
admin.site.register(inventarios, InventariosAdmin)
