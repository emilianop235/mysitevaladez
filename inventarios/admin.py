from django.contrib import admin
from .models import inventarios


class InventariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cantidad', 'ubicacion')
admin.site.register(inventarios, InventariosAdmin)