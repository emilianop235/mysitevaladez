from django.urls import path
from .views import listar_inactivos, listargrupos, listar_todos_grupos, creargrupo, desactivargrupo, editargrupo, consultargrupo, restaurargrupo

urlpatterns = [
    path('', listargrupos),
    path('todos/', listar_todos_grupos),
    path('nuevo/', creargrupo),
    path('desactivar/<int:id>/', desactivargrupo),
    path('editar/<int:id>/', editargrupo),
    path('consultar/<int:id>/', consultargrupo),
    path('inactivos/', listar_inactivos, name='listar_inactivos'),
    path('restaurar/<int:id>/', restaurargrupo, name='restaurargrupo'),
]