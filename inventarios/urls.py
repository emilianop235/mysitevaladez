from django.urls import path
from .views import (
    listar_inactivos,
    listarinventarios, 
    listar_todos_inventarios, 
    crearinventario, 
    desactivarinventario, 
    editarinventario, 
    consultarinventario,
    restaurarinventario
)

urlpatterns = [
    path('', listarinventarios),
    path('todos/', listar_todos_inventarios),
    path('nuevo/', crearinventario),
    path('desactivar/<int:id>/', desactivarinventario),
    path('editar/<int:id>/', editarinventario),
    path('consultar/<int:id>/', consultarinventario),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurarinventario, name='restaurarinventario'),
]