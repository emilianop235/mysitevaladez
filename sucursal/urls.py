from django.urls import path
from .views import listarsucursales, crearsucursal

urlpatterns = [
    path('', listarsucursales),
    path('nuevo/', crearsucursal),
]