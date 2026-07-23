from django.contrib import admin
from ventas.models import ventas

class VentasAdmin(admin.ModelAdmin):
    list_display = ('id', 'folio', 'fecha', 'total', 'estatus')
    search_fields = ('folio', 'cliente__nombre', 'cliente__apellido', 'producto__nombre')
    list_filter = ('estatus', 'fecha')
    ordering = ('-fecha',)
admin.site.register(ventas, VentasAdmin)
