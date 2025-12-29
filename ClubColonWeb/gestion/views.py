from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Socio, Deporte, PagoCuota, Perfil
from .forms import (
    SocioForm, DeporteForm, PagoCuotaForm, 
    BusquedaSocioForm, RegistroForm, PerfilForm
)

# Vista de Inicio - Pública
def inicio(request):
    mensaje = request.GET.get('mensaje') 
    return render(request, 'gestion/inicio.html', {'mensaje': mensaje})

# --- Vistas Protegidas (Solo usuarios logueados) ---

@login_required
def nuevo_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('inicio') + '?mensaje=✅ Socio registrado correctamente.')
    else:
        form = SocioForm()
    return render(request, 'gestion/formulario_socio.html', {'titulo': 'Registrar Nuevo Socio', 'form': form})

@login_required
def nuevo_deporte(request):
    if request.method == 'POST':
        form = DeporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('inicio') + '?mensaje=✅ Deporte agregado correctamente.')
    else:
        form = DeporteForm()
    return render(request, 'gestion/formulario_deporte.html', {'titulo': 'Agregar Actividad Deportiva', 'form': form})

@login_required
def registrar_pago(request):
    if request.method == 'POST':
        form = PagoCuotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('inicio') + '?mensaje=✅ Pago registrado con éxito.')
    else:
        form = PagoCuotaForm()
    return render(request, 'gestion/formulario_pago.html', {'titulo': 'Registrar Pago de Cuota', 'form': form})

# --- Búsqueda, Registro y Perfil ---

def buscar_socio(request):
    formulario = BusquedaSocioForm(request.GET or None)
    info = request.GET.get('criterio', '').strip()
    resultados = []
    busqueda_activa = False
    

    if info:
        resultados = Socio.objects.filter(apellido__icontains=info)
        busqueda_activa = True

    return render(request, 'gestion/buscar_socio.html', {
        'form': formulario, 'socios': resultados, 'busqueda_activa': busqueda_activa
    })

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'gestion/registro.html', {'form': form})

@login_required
def editar_perfil(request):
    # Intentamos obtener el perfil, si no existe lo crea (por seguridad)
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'gestion/editar_perfil.html', {'form': form})

def acerca_de_mi(request):
    return render(request, 'gestion/acerca_de_mi.html')

@login_required
def editar_socio(request, id):
    socio = Socio.objects.get(id=id)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('buscar_socio')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'gestion/formulario_socio.html', {'form': form, 'titulo': 'Editar Socio'})

@login_required
def eliminar_socio(request, id):
    socio = Socio.objects.get(id=id)
    if request.method == 'POST':
        socio.delete()
        return redirect('buscar_socio')
    return render(request, 'gestion/confirmar_eliminar.html', {'socio': socio})