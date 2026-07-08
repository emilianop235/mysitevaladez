from django.db import models

class nomina(models.Model):
    numperiodo = models.CharField(max_length=50)
    fecha = models.DateField()
    salario = models.FloatField()
    perceciones = models.FloatField() # Mantenemos el nombre exacto de tu rúbrica
    deducciones = models.FloatField()
    total = models.FloatField()
    
    # Llave foránea conectada a tu clase empleados en minúscula
    empleado = models.ForeignKey('empleados.Empleado', on_delete=models.CASCADE, related_name='nominas')

    def __str__(self):
        return f"Periodo {self.numperiodo} - {self.empleado.nombre}"