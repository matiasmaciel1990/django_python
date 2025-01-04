from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Renderiza una plantilla

def clientes(request):
    return HttpResponse("Hola, ¿cómo estás?")  # Muestra el mensaje