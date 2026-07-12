from django.urls import path
from .views import (
    listarproveedores, 
    listar_todos_proveedores, 
    crearproveedor, 
    desactivarproveedor, 
    editarproveedor, 
    consultarproveedor
)

urlpatterns = [
    path('', listarproveedores),
    path('todos/', listar_todos_proveedores),
    path('nuevo/', crearproveedor),
    path('desactivar/<int:id>/', desactivarproveedor),
    path('editar/<int:id>/', editarproveedor),
    path('consultar/<int:id>/', consultarproveedor),
]