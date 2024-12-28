from django.db import models

# Create your models here.

class Pedido(models.Model):
    numero = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetallePedido')

    def __str__(self):
        return f"Pedido #{self.numero} - Cliente: {self.cliente.nombre}"