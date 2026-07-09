from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)

    status = models.BooleanField(default=True)


def __str__(self):
    return self.nombre



