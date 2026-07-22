from django.contrib import admin
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'telefono')
admin.site.register(Empleado, EmpleadoAdmin)