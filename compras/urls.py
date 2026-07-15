from django.urls import path
from .views import listar_inactivos, listarcompras, listar_todas_compras, crearcompra, desactivarcompra, editarcompra, consultarcompra, restaurarcompra

urlpatterns = [
    path('', listarcompras),
    path('todos/', listar_todas_compras),
    path('nuevo/', crearcompra),
    path('desactivar/<int:id>/', desactivarcompra),
    path('editar/<int:id>/', editarcompra),
    path('consultar/<int:id>/', consultarcompra),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurarcompra, name='restaurarcompra'),
]