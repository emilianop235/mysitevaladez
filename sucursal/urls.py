from django.urls import path
from .views import (
    listar_inactivos,
    listarsucursales, 
    listar_todas_sucursales, 
    crearsucursal, 
    desactivarsucursal, 
    editarsucursal, 
    consultarsucursal,
    restaurarsucursal
)

urlpatterns = [
    path('', listarsucursales),
    path('todos/', listar_todas_sucursales),
    path('nuevo/', crearsucursal),
    path('desactivar/<int:id>/', desactivarsucursal),
    path('editar/<int:id>/', editarsucursal),
    path('consultar/<int:id>/', consultarsucursal),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurarsucursal, name='restaurarsucursal'),
]