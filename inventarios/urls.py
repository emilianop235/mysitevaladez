from django.urls import path
from .views import (
    listarinventarios, 
    listar_todos_inventarios, 
    crearinventario, 
    desactivarinventario, 
    editarinventario, 
    consultarinventario
)

urlpatterns = [
    path('', listarinventarios),
    path('todos/', listar_todos_inventarios),
    path('nuevo/', crearinventario),
    path('desactivar/<int:id>/', desactivarinventario),
    path('editar/<int:id>/', editarinventario),
    path('consultar/<int:id>/', consultarinventario),
]