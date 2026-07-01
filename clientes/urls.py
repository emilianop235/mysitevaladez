from django.urls import path
from .views import listaclientes, crearclientes

urlpatterns = [
    path('', listaclientes),          
    path('nuevo/', crearclientes)      
]