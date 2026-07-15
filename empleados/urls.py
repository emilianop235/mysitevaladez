from django.urls import path
from .views import (
    listar_inactivos, listarempleados, listar_todos_empleados, crearempleado, 
    desactivarempleado, editarempleado, consultarempleado, restaurarempleado,
    # Si tienes las de nómina, impórtalas también: listarnominas, crearnomina
)

urlpatterns = [
    path('', listarempleados),
    path('todos/', listar_todos_empleados),
    path('nuevo/', crearempleado),
    path('desactivar/<int:id>/', desactivarempleado),
    path('editar/<int:id>/', editarempleado),
    path('consultar/<int:id>/', consultarempleado),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurarempleado, name='restaurarempleado'),
]