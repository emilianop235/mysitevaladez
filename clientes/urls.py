from django.urls import path
from .views import listarclientes, listar_todos_clientes, crearcliente, desactivarcliente, editarcliente, consultarcliente

urlpatterns = [
    path('', listarclientes),
    path('todos/', listar_todos_clientes),
    path('nuevo/', crearcliente),
    path('desactivar/<int:id>/', desactivarcliente),
    path('editar/<int:id>/', editarcliente),
    path('consultar/<int:id>/', consultarcliente),
]