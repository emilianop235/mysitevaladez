from django.urls import path
from .views import listarproveedores, crearproveedor

urlpatterns = [
    path('', listarproveedores),
    path('nuevo/', crearproveedor),
]