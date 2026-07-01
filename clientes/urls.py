from django.urls import path
from .views import clientes, crearclientes

urlpatterns = [
    path('', clientes),
    path('nuevo/', crearclientes)
]