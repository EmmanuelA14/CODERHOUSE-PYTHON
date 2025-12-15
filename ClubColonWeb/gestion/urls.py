from django.shortcuts import render
from django.http import HttpResponse

# Vista principal que renderiza la plantilla de inicio.
def inicio(request):
    # 'mensaje' es solo un ejemplo, puedes pasar datos dinámicos aquí.
    mensaje = "¡Bienvenido al Panel de Gestión!"
    return render(request, 'gestion/inicio.html', {'mensaje': mensaje})

# --- Vistas Placeholder para navegación de base.html ---

def crear_socio(request):
    # Renderiza una plantilla genérica para las nuevas URLs
    return render(request, 'gestion/placeholder.html', {'title': 'Crear Nuevo Socio'})

def crear_deporte(request):
    return render(request, 'gestion/placeholder.html', {'title': 'Crear Nuevo Deporte'})

def registrar_pago(request):
    return render(request, 'gestion/placeholder.html', {'title': 'Registrar Pago de Socio'})

def buscar_socio(request):
    return render(request, 'gestion/placeholder.html', {'title': 'Buscar Socios'})