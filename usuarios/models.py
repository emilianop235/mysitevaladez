from django.db import models

class usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    correo = models.EmailField()
    # Referencia en texto, con null=True para evitar choques con datos viejos
    grupo = models.ForeignKey('grupos.grupos', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.usuario