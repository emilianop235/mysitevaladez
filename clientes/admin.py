from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'sexo', 'tipo', 'estatus')
    search_fields = ('nombre', 'apellido', 'direccion')
    list_filter = ('sexo', 'tipo', 'estatus')
    ordering = ('nombre', 'apellido')


admin.site.register(Cliente, ClienteAdmin)
