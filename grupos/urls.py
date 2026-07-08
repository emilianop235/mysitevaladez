from django.urls import path
from .views import listargrupos, creargrupo

urlpatterns = [
    path('', listargrupos),
    path('nuevo/', creargrupo),
]