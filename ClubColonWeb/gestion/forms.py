from django import forms
from .models import Deporte, Socio, PagoCuota , Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Formulario 1: Carga de Deportes (Modelo Deporte)
class DeporteForm(forms.ModelForm):
    """
    Formulario para agregar una nueva actividad deportiva al club.
    """
    class Meta:
        model = Deporte
        fields = '__all__'
        # Widgets para aplicar estilos de Bootstrap
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Fútbol'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Primera División'}),
            'cuota_adicional': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Costo extra por el deporte'}),
        }

# Formulario 2: Carga de Socios (Modelo Socio)
class SocioForm(forms.ModelForm):
    """
    Formulario para registrar un nuevo Socio.
    """
    class Meta:
        model = Socio
        fields = '__all__'
        # Se utilizan widgets específicos para fechas y estilos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            # Importante: usar type='date' para el selector de calendario HTML5
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # Checkbox simple
            'es_familiar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Formulario 3: Registro de Pagos (Modelo PagoCuota)
class PagoCuotaForm(forms.ModelForm):
    """
    Formulario para registrar un pago de cuota, incluyendo una relación FK a Socio.
    """
    class Meta:
        model = PagoCuota
        # El campo 'fecha_pago' se omite porque se añade automáticamente (auto_now_add=True)
        fields = ['socio', 'monto', 'detalle']
        widgets = {
            # Select de socios disponibles (ForeignKey)
            'socio': forms.Select(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto pagado'}),
            'detalle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Cuota Enero 2025'}),
        }

# Formulario de Búsqueda
class BusquedaSocioForm(forms.Form):
    """
    Formulario simple para buscar Socios por criterio (apellido).
    """
    criterio = forms.CharField(
        max_length=50, 
        label='Buscar Socio',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Buscar por apellido, Ej: López'
        })
    )
# Formulario de Registro de Usuario y Perfil
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar']