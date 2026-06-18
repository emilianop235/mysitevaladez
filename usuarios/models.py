from django.db import models

class usuario(models.Model):
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)