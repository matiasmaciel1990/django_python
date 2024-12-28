from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    descuento = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre