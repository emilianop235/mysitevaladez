from django.urls import path
from .views import (
    listarproductos, 
    listar_todos_productos, 
    crearproducto, 
    desactivarproducto, 
    editarproducto, 
    consultarproducto
)

urlpatterns = [
    path('', listarproductos),
    path('todos/', listar_todos_productos),
    path('nuevo/', crearproducto),
    path('desactivar/<int:id>/', desactivarproducto),
    path('editar/<int:id>/', editarproducto),
    path('consultar/<int:id>/', consultarproducto),
]