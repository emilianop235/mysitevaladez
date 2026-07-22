from django.contrib import admin
from nomina.models import nomina


class NominaAdmin(admin.ModelAdmin):
    list_display = ('id', 'empleado', 'salario', 'fecha_pago')

admin.site.register(nomina, NominaAdmin)