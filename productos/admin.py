from django.contrib import admin
from .models import producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'stock')
admin.site.register(producto, ProductoAdmin)