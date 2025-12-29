from django.urls import path
from . import views  # Aquí importamos el archivo de vistas que me pasaste

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevo-socio/', views.nuevo_socio, name='nuevo_socio'),
    path('nuevo-deporte/', views.nuevo_deporte, name='nuevo_deporte'),
    path('registrar-pago/', views.registrar_pago, name='registrar_pago'),
    path('buscar-socio/', views.buscar_socio, name='buscar_socio'),
    path('registro/', views.registro, name='registro'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('editar-socio/<int:id>/', views.editar_socio, name='editar_socio'),
    path('eliminar-socio/<int:id>/', views.eliminar_socio, name='eliminar_socio'),
]