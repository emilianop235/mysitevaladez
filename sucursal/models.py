from django.db import models

class sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    encargado = models.CharField(max_length=100, default="Por asignar")
    
    # Campo para borrado lógico
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre