from django.db import models

class ventas(models.Model):
    # auto_now_add registra en automático la fecha exacta del momento de la compra
    fecha = models.DateTimeField(auto_now_add=True) 
    cantidad = models.IntegerField(default=1) # <- Agregado para poder registrar el volumen vendido
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Tus relaciones perfectamente definidas apuntando a tus apps
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    empleado = models.ForeignKey('empleados.Empleado', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.cliente.nombre} - Total: {self.total}"