from django.db import models

from clientes.models import Cliente
from productos.models import Producto

# Create your models here.

class Pedido(models.Model):
    numero = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetallePedido')

    def __str__(self):
        return f"Pedido #{self.numero} - Cliente: {self.cliente.nombre}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Pedido {self.pedido.id})"