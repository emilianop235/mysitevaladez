from django.urls import path
from .views import listarnominas, crearnomina

urlpatterns = [
    path('nominas/', listarnominas),
    path('nominas/nuevo/', crearnomina),
]