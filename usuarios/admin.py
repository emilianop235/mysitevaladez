from django.contrib import admin

from usuarios.models import usuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
admin.site.register(usuarios, UsuariosAdmin)