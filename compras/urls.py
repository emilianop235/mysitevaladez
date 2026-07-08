from django.urls import path
from .views import listarcompras, crearcompra

urlpatterns = [
    path('', listarcompras),
    path('nuevo/', crearcompra),
]