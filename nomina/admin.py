from django.contrib import admin
from nomina.models import nomina


class NominaAdmin(admin.ModelAdmin):
    list_display = ('id', 'empleado', 'salario', 'fecha')
    search_fields = ('numperiodo', 'empleado__nombre', 'empleado__apellido')
    list_filter = ('estatus', 'fecha')
    ordering = ('-fecha',)

admin.site.register(nomina, NominaAdmin)
