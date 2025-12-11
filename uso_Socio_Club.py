import Socio_club # Importa el archivo socio_club.py
from datetime import datetime

# La clase 'Socio' se accede a través del módulo 'socio_club'

print("=====================================================")
print("      CLUB ATLÉTICO COLÓN DE SANTA FE - GESTIÓN")
print("=====================================================")

# 1. Socio Cadete (Edad <= 16, descuento 20%) - ID 1000
socio1 = Socio_club.Socio("Bautista Aglieri", "2010-10-15", 2024, es_familiar=False)

# 2. Socio Activo (Edad > 16, Antigüedad < 35, cuota plena) - ID 1001
socio2 = Socio_club.Socio("Josefina Risso", "1982-10-20", 2015, es_familiar=True)

# 3. Socio Vitalicio (Antigüedad >= 35, bonificación 100%) - ID 1002
current_year = datetime.now().year
socio3 = Socio_club.Socio("Ricardo Orlando Aglieri", "1945-02-06", 1985, es_familiar=False)

print("\n--- Socio 1: CADETE ---")
print(socio1)

print("\n--- Socio 2: ACTIVO (Familiar) ---")
print(socio2)

print("\n--- Socio 3: VITALICIO ---")
print(socio3)

print("\n--- Pruebas de Métodos ---")

# Prueba de cálculo de cuota para Activo Familiar
print(f"La cuota de {socio2.nombre} (Activo Familiar) es: ${socio2.calcular_cuota():.2f}")

# Pruebas de la Bonificación Total
if socio3.calcular_cuota() == 0.0:
    print(f"La cuota de {socio3.nombre} (Vitalicio) es correctamente bonificada (0.00).")
else:
    print(f"Error en la bonificación de Vitalicio. Cuota calculada: ${socio3.calcular_cuota():.2f}")

print("=====================================================")