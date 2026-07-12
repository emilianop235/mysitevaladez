from django.db import models

class ventas(models.Model):
    folio = models.CharField(max_length=50, default='V-001')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0.0)
    
    cliente = models.ManyToManyField('clientes.Cliente')
    producto = models.ManyToManyField('productos.Producto')

    # Campo para borrado lógico
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.folio