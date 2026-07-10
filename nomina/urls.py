from django.urls import path
from .views import (
    listarnominas, 
    listar_todas_nominas, 
    crearnomina, 
    desactivarnomina, 
    editarnomina, 
    consultarnomina
)

urlpatterns = [
    path('', listarnominas),
    path('todos/', listar_todas_nominas),
    path('nuevo/', crearnomina),
    path('desactivar/<int:id>/', desactivarnomina),
    path('editar/<int:id>/', editarnomina),
    path('consultar/<int:id>/', consultarnomina),
]