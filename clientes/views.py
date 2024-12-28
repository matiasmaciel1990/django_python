from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vista_inicio(request):
    return HttpResponse("¡Bienvenido a la gestión de clientes!")