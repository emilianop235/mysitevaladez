from django.contrib import admin
from .models import compras

class ComprasAdmin(admin.ModelAdmin):
    list_display = ('id', 'folio', 'fecha', 'subtotal', 'iva', 'total', 'estatus')
    search_fields = ('folio', 'proveedor__nombre', 'producto__nombre')
    list_filter = ('estatus', 'fecha')
    ordering = ('-fecha',)

admin.site.register(compras, ComprasAdmin)
