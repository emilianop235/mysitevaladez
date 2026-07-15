from django.urls import path
from .views import (
    pageempleados,
    pageempleados_todos,
    nuevo_empleado,
    editar_empleado,
    consultar_empleado,
    desactivar_empleado,
    listar_inactivos,
    restaurarempleado,
)

urlpatterns = [
    path('', pageempleados),
    path('todos/', pageempleados_todos),
    path('nuevo/', nuevo_empleado),
    path('desactivar/<int:id>/', desactivar_empleado),
    path('editar/<int:id>/', editar_empleado),
    path('consultar/<int:id>/', consultar_empleado),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurarempleado, name='restaurarempleado'),
]