from django.urls import path
from .views import (
    listarsucursales, 
    listar_todas_sucursales, 
    crearsucursal, 
    desactivarsucursal, 
    editarsucursal, 
    consultarsucursal
)

urlpatterns = [
    path('', listarsucursales),
    path('todos/', listar_todas_sucursales),
    path('nuevo/', crearsucursal),
    path('desactivar/<int:id>/', desactivarsucursal),
    path('editar/<int:id>/', editarsucursal),
    path('consultar/<int:id>/', consultarsucursal),
]