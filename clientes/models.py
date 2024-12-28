from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)    # Dirección física
    telefono = models.CharField(max_length=20)      # Teléfono de contacto
    email = models.EmailField(unique=True)          # Correo electrónico único

    descuento = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre