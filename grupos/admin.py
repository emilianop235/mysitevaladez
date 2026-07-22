from django.contrib import admin
from .models import grupos


class GruposAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
admin.site.register(grupos, GruposAdmin)