from django.urls import path
from . import views

# Define el namespace de la aplicación para evitar conflictos de nombres
app_name = 'gestion'

urlpatterns = [
    # 1. Ruta de Inicio (Dashboard principal del sistema de gestión)
    path('', views.inicio, name='inicio'),

    # 2. Ruta para el formulario de creación de un nuevo socio
    path('crear-socio/', views.nuevo_socio, name='crear_socio'),
    
    # 3. Ruta para el formulario de creación de un nuevo deporte/actividad
    path('crear-deporte/', views.nuevo_deporte, name='crear_deporte'),
    
    # 4. Ruta para registrar un nuevo pago de cuota
    path('registrar-pago/', views.registrar_pago, name='registrar_pago'),

    # 5. Ruta para la funcionalidad de búsqueda de socios o registros
    path('buscar-socio/', views.buscar_socio, name='buscar_socio'),

    # NOTA: Asegúrate de que todas estas funciones estén definidas en gestion/views.py
]