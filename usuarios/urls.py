from django.urls import path
from .views import validar_login, listar_usuarios, crear_usuario

urlpatterns = [
    path('', listar_usuarios),          # Carga la tabla con el menú lateral
    path('nuevo/', crear_usuario),      # Procesa el formulario de registro
    path('login/', validar_login),      # Mantiene la ruta de acceso independiente
]