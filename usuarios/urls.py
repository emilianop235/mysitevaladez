from django.urls import path


from .views import (
    listar_inactivos,
    listarusuarios, 
    listar_todos_usuarios, 
    crearusuario, 
    desactivarusuario, 
    editarusuario, 
    consultarusuario,
    restaurarusuario
)

urlpatterns = [
    path('', listarusuarios),
    path('todos/', listar_todos_usuarios),
    path('nuevo/', crearusuario),
    path('desactivar/<int:id>/', desactivarusuario),
    path('editar/<int:id>/', editarusuario),
    path('consultar/<int:id>/', consultarusuario),
    path('inactivos/',listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/',restaurarusuario, name='restaurarusuario'),
]