from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fabricante = models.CharField(max_length=100)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre