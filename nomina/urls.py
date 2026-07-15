from django.urls import path
from .views import (
    listar_inactivos,
    listarnominas, 
    listar_todas_nominas, 
    crearnomina, 
    desactivarnomina, 
    editarnomina, 
    consultarnomina,
    restaurarnomina
)

urlpatterns = [
    path('', listarnominas),
    path('todos/', listar_todas_nominas),
    path('nuevo/', crearnomina),
    path('desactivar/<int:id>/', desactivarnomina),
    path('editar/<int:id>/', editarnomina),
    path('consultar/<int:id>/', consultarnomina),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurarnomina, name='restaurarnomina'),
]