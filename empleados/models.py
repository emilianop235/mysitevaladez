from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    salario_base = models.FloatField(default=0.0) # Nuevo dato fijo
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"