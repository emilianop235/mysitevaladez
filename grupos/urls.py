from django.urls import path
from .views import listargrupos, listar_todos_grupos, creargrupo, desactivargrupo, editargrupo, consultargrupo

urlpatterns = [
    path('', listargrupos),
    path('todos/', listar_todos_grupos),
    path('nuevo/', creargrupo),
    path('desactivar/<int:id>/', desactivargrupo),
    path('editar/<int:id>/', editargrupo),
    path('consultar/<int:id>/', consultargrupo),
]