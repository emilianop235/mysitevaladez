from django.urls import path
from .views import listar_inventarios, crear_inventario

urlpatterns = [
    path('', listar_inventarios),
    path('nuevo/', crear_inventario),
]