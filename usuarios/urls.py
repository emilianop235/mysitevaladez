from django.urls import path
from .views import validar_login

urlpatterns = [
    path('', validar_login),          # Muestra el login
    path('login/', validar_login),    # Recibe los datos del formulario
]