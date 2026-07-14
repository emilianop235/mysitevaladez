from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"