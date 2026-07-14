from django.db import models

class nomina(models.Model):
    numperiodo = models.CharField(max_length=50)
    fecha = models.DateField()
    salario = models.FloatField()
    perceciones = models.FloatField()  # Variable exacta del PDF
    deducciones = models.FloatField()
    total = models.FloatField()
    empleado = models.ForeignKey('empleados.Empleado', on_delete=models.CASCADE, related_name='nominas')
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"Periodo {self.numperiodo} - {self.empleado.nombre}"