from django.urls import path
from .views import (
    listarusuarios, 
    listar_todos_usuarios, 
    crearusuario, 
    desactivarusuario, 
    editarusuario, 
    consultarusuario
)

urlpatterns = [
    path('', listarusuarios),
    path('todos/', listar_todos_usuarios),
    path('nuevo/', crearusuario),
    path('desactivar/<int:id>/', desactivarusuario),
    path('editar/<int:id>/', editarusuario),
    path('consultar/<int:id>/', consultarusuario),
]