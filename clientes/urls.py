from django.urls import path

from .views import listarclientes, listar_todos_clientes, crearcliente, desactivarcliente, editarcliente, consultarcliente, listar_inactivos, restaurarcliente

urlpatterns = [
    path('', listarclientes),
    path('todos/', listar_todos_clientes),
    path('nuevo/', crearcliente),
    path('desactivar/<int:id>/', desactivarcliente),
    path('editar/<int:id>/', editarcliente),
    path('consultar/<int:id>/', consultarcliente),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurarcliente, name='restaurarcliente'),
]