from django.db import models
from datetime import date

# Modelo 1: Deporte (Actividades del club)
class Deporte(models.Model):
    # Nombre de la actividad (Ej: Fútbol, Tenis)
    nombre = models.CharField(max_length=50)
    # Categoría o grupo de edad (Ej: Infantil, Primera)
    categoria = models.CharField(max_length=50) 
    # Cuota extra por practicar este deporte
    cuota_adicional = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

# Modelo 2: Socio (Adaptación de tu clase Python a Django DB)
class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField()
    # Fecha para calcular la antigüedad
    fecha_ingreso = models.DateField() 
    # Indica si es socio familiar (para descuentos de cuotas, aunque no se usa en esta versión web)
    es_familiar = models.BooleanField(default=False)
    
    # Lógica de negocio para calcular edad
    def calcular_edad(self):
        today = date.today()
        # Calcula la edad precisa
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    # Lógica de negocio para calcular antigüedad
    def calcular_antiguedad(self):
        today = date.today()
        return today.year - self.fecha_ingreso.year

    # Lógica de negocio para determinar la categoría del club
    def obtener_categoria(self):
        edad = self.calcular_edad()
        antiguedad = self.calcular_antiguedad()
        
        if edad <= 16:
            return "Cadete"
        # Vitalicio: Antigüedad >= 35 
        elif antiguedad >= 35:
            return "Vitalicio"
        else:
            # Activo: Edad > 16 y Antigüedad < 35
            return "Activo"

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.obtener_categoria()}"

# Modelo 3: PagoCuota (Registro de transacciones)
class PagoCuota(models.Model):
    # Relación uno a muchos: Un socio puede tener muchos pagos
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    # Se añade automáticamente la fecha actual
    fecha_pago = models.DateField(auto_now_add=True)
    # Descripción del pago (Ej: Cuota Social, Cuota Fútbol)
    detalle = models.CharField(max_length=100, default="Cuota Social")

    def __str__(self):
        return f"Pago de {self.socio}: ${self.monto}"