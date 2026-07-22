from django.contrib import admin
from .models import compras

class ComprasAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cantidad', 'precio')

admin.site.register(compras, ComprasAdmin)