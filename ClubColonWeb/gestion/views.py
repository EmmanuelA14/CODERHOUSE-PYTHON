from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Socio, Deporte, PagoCuota
from .forms import SocioForm, DeporteForm, PagoCuotaForm, BusquedaSocioForm

# Vista de Inicio
def inicio(request):
    """Muestra la página de inicio."""
    # El mensaje se puede pasar desde otras vistas usando el contexto
    mensaje = request.GET.get('mensaje') 
    return render(request, 'gestion/inicio.html', {'mensaje': mensaje})

# --- Vistas de Carga de Datos (Formularios) ---

def nuevo_socio(request):
    """Maneja la creación de un nuevo Socio."""
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar a inicio con un mensaje de éxito
            return redirect(reverse('inicio') + '?mensaje=✅ Socio registrado correctamente.')
    else:
        form = SocioForm()
    
    context = {
        'titulo': 'Registrar Nuevo Socio',
        'form': form
    }
    return render(request, 'gestion/formulario_socio.html', context)

def nuevo_deporte(request):
    """Maneja la creación de un nuevo Deporte."""
    if request.method == 'POST':
        form = DeporteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar a inicio con un mensaje de éxito
            return redirect(reverse('inicio') + '?mensaje=✅ Deporte agregado correctamente.')
    else:
        form = DeporteForm()

    context = {
        'titulo': 'Agregar Actividad Deportiva',
        'form': form
    }
    return render(request, 'gestion/formulario_deporte.html', context)

def registrar_pago(request):
    """Maneja el registro de un PagoCuota."""
    if request.method == 'POST':
        form = PagoCuotaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar a inicio con un mensaje de éxito
            return redirect(reverse('inicio') + '?mensaje=✅ Pago registrado con éxito.')
    else:
        form = PagoCuotaForm()

    context = {
        'titulo': 'Registrar Pago de Cuota',
        'form': form
    }
    return render(request, 'gestion/formulario_pago.html', context)

# --- Vista de Búsqueda ---

def buscar_socio(request):
    """
    Muestra el formulario de búsqueda y los resultados si se realiza una consulta.
    La búsqueda se realiza por apellido.
    """
    formulario = BusquedaSocioForm(request.GET or None)
    resultados = []
    busqueda_activa = False
    info = ''

    # Verificar si se ha enviado el formulario de búsqueda (método GET)
    if formulario.is_valid():
        info = formulario.cleaned_data.get('criterio')
        if info:
            # Filtra la base de datos: 'apellido__icontains' busca coincidencias ignorando mayúsculas/minúsculas
            resultados = Socio.objects.filter(apellido__icontains=info)
            busqueda_activa = True

    context = {
        'titulo': 'Buscar Socio',
        'form': formulario,
        'socios': resultados,
        'busqueda': info,
        'busqueda_activa': busqueda_activa
    }
    
    # Se utiliza una única plantilla para mostrar el formulario y los resultados
    return render(request, 'gestion/buscar_socio.html', context)