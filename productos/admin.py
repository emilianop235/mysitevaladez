from django.contrib import admin
from .models import producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'estatus')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('estatus',)
    ordering = ('nombre',)
admin.site.register(producto, ProductoAdmin)
