from django.urls import path
from .views import listar_ventas, crear_venta

urlpatterns = [
    path('', listar_ventas),
    path('nuevo/', crear_venta),
]