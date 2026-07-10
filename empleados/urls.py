from django.urls import path
from .views import (
    listarempleados, listar_todos_empleados, crearempleado, 
    desactivarempleado, editarempleado, consultarempleado,
    # Si tienes las de nómina, impórtalas también: listarnominas, crearnomina
)

urlpatterns = [
    path('', listarempleados),
    path('todos/', listar_todos_empleados),
    path('nuevo/', crearempleado),
    path('desactivar/<int:id>/', desactivarempleado),
    path('editar/<int:id>/', editarempleado),
    path('consultar/<int:id>/', consultarempleado),
    
    # path('nominas/', listarnominas),
    # path('nominas/nuevo/', crearnomina),
]