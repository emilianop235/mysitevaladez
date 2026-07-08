from django.urls import path
from .views import listarnominas, crearnomina

urlpatterns = [
    path('', listarnominas),
    path('nuevo/', crearnomina),
]