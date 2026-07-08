from django.db import models

class compra(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1) 
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre