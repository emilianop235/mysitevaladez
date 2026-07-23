from django.contrib import admin

from usuarios.models import usuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'correo', 'grupo', 'estatus')
    search_fields = ('nombre', 'usuario', 'correo', 'grupo__nombre')
    list_filter = ('estatus', 'grupo')
    ordering = ('usuario',)
admin.site.register(usuarios, UsuariosAdmin)
