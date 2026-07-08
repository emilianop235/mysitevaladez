from django.db import models

class inventarios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1)
    fecha_income = models.DateTimeField(auto_now_add=True) # Adaptado de tu fecha_ingreso

    def __str__(self):
        return self.nombre