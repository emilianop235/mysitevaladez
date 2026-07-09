from django.db import models

class compras(models.Model):
    folio = models.CharField(max_length=50, default='C-001')
    fecha = models.DateField()
    subtotal = models.FloatField(default=0.0)
    iva = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)
    
    proveedor = models.ManyToManyField('proveedores.proveedores')
    producto = models.ManyToManyField('productos.Producto')
    
    # Campo para borrado lógico
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.folio