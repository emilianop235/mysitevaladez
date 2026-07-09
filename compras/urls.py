from django.urls import path
from .views import listarcompras, listar_todas_compras, crearcompra, desactivarcompra, editarcompra, consultarcompra

urlpatterns = [
    path('', listarcompras),
    path('todos/', listar_todas_compras),
    path('nuevo/', crearcompra),
    path('desactivar/<int:id>/', desactivarcompra),
    path('editar/<int:id>/', editarcompra),
    path('consultar/<int:id>/', consultarcompra),
]