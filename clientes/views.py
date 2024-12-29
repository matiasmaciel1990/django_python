from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Cliente

def vista_inicio(request):
    return HttpResponse("¡Bienvenido a la gestión de clientes!")


# Crear nuevo cliente
def crear_cliente(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        descuento = request.POST['descuento']
        Cliente.objects.create(nombre=nombre, email=email, descuento=descuento)
        return HttpResponseRedirect('/clientes/')  # Redirigir a la lista de clientes
    return render(request, 'clientes/crear_cliente.html')

# Modificar cliente
def modificar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        cliente.nombre = request.POST['nombre']
        cliente.email = request.POST['email']
        cliente.descuento = request.POST['descuento']
        cliente.save()
        return HttpResponseRedirect('/clientes/')  # Redirigir a la lista de clientes
    return render(request, 'clientes/modificar_cliente.html', {'cliente': cliente})

# Eliminar cliente
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        cliente.delete()
        return HttpResponseRedirect('/clientes/')  # Redirigir a la lista de clientes
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})

# Visualizar cliente
def visualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/visualizar_cliente.html', {'cliente': cliente})

# Listar clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})
