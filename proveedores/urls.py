from django.urls import path
from .views import (
    listar_inactivos,
    listarproveedores, 
    listar_todos_proveedores, 
    crearproveedor, 
    desactivarproveedor, 
    editarproveedor, 
    consultarproveedor,
    restaurarproveedor
)

urlpatterns = [
    path('', listarproveedores),
    path('todos/', listar_todos_proveedores),
    path('nuevo/', crearproveedor),
    path('desactivar/<int:id>/', desactivarproveedor),
    path('editar/<int:id>/', editarproveedor),
    path('consultar/<int:id>/', consultarproveedor),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurarproveedor, name='restaurarproveedor'),
]