from django.db import models
from productos.models import producto
from proveedores.models import proveedores as ModeloProveedor
from sucursal.models import sucursal as ModeloSucursal # Importamos con alias por seguridad

class inventarios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1)
    fecha_income = models.DateTimeField(auto_now_add=True)
    estatus = models.BooleanField(default=True)


    producto_relacionado = models.ForeignKey(producto, on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey(ModeloProveedor, on_delete=models.SET_NULL, null=True, blank=True)
    sucursal = models.ForeignKey(ModeloSucursal, on_delete=models.SET_NULL, null=True, blank=True) # <-- NUEVO
    ubicacion = models.CharField(max_length=100, default='Almacén General')

    def __str__(self):
        return self.nombre