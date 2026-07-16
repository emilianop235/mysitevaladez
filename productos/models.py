from django.db import models

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre