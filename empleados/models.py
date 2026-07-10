from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    
    # Campo para borrado lógico
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class nomina(models.Model):
    numperiodo = models.CharField(max_length=50)
    fecha = models.DateField()
    salario = models.FloatField()
    percepciones = models.FloatField()
    deducciones = models.FloatField()
    total = models.FloatField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='nominas')

    def __str__(self):
        return f"Periodo {self.numperiodo} - {self.empleado.nombre}"