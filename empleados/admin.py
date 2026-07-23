from django.contrib import admin
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'sexo', 'tipo', 'salario_base', 'estatus')
    search_fields = ('nombre', 'apellido', 'tipo')
    list_filter = ('sexo', 'tipo', 'estatus')
    ordering = ('nombre', 'apellido')
admin.site.register(Empleado, EmpleadoAdmin)
