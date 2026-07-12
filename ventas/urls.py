from django.urls import path
from .views import (
    listarventas, 
    listar_todas_ventas, 
    crearventa, 
    desactivarventa, 
    editarventa, 
    consultarventa
)

urlpatterns = [
    path('', listarventas),
    path('todos/', listar_todas_ventas),
    path('nuevo/', crearventa),
    path('desactivar/<int:id>/', desactivarventa),
    path('editar/<int:id>/', editarventa),
    path('consultar/<int:id>/', consultarventa),
]