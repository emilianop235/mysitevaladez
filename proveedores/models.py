from django.db import models

class proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    
    # Agregamos estatus para el borrado lógico de proveedores
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class productos(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    peso = models.FloatField()
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    color = models.CharField(max_length=1000)
    
    # Lo agregamos aquí también por si acaso llegas a usar esta tabla
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre