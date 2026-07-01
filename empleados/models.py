from django.db import models

import empleados

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)


class nomina(models.Model):
    numperiodo = models.CharField()
    fecha = models.DateField()
    salario = models.FloatField()
    percepciones = models.FloatField()
    deducciones = models.FloatField()
    total = models.FloatField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='nomina')