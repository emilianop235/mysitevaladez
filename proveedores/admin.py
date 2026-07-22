from django.contrib import admin
from .models import proveedores

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono')

admin.site.register(proveedores, ProveedoresAdmin)