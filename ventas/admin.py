from django.contrib import admin
from ventas.models import ventas

class VentasAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cantidad', 'precio', 'fecha_venta')
admin.site.register(ventas, VentasAdmin)