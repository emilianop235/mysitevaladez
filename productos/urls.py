from django.urls import path
from .views import listarproductos, crearproducto

urlpatterns = [
    # La ruta vacía lista los productos y 'nuevo/' procesa el formulario
    path('', listarproductos),
    path('nuevo/', crearproducto),
]