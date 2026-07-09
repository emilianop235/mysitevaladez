from django.db import models

class grupos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    estatus = models.BooleanField(default=True)          

    def __str__(self):
        return self.nombre