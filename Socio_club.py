from datetime import datetime

class Socio:
    # hay 3 categorias de socios con cuotas dinamicas    
    # Atributo de CLASE 1: Contador para generar IDs numéricos secuenciales.
    _conteo_socio = 1000 
    
    # Atributo de CLASE 2 : Precio base de la cuota mensual.
    CUOTA_BASE = 30000.00
    
    def __init__(self, nombre: str, fecha_nacimiento: str, anio_ingreso: int, es_familiar: bool = False):
        # Método para los atributos del socio.         
        # Atributos de Instancia (Mínimo 4 requeridos): socio_id, nombre, edad (calculada), - antiguedad (calculada)
        
        self.socio_id = Socio._conteo_socio
        Socio._conteo_socio += 1# Incrementa el contador de clase para el siguiente cliente
        self.nombre = nombre
        self.es_familiar = es_familiar
        self.anio_ingreso = anio_ingreso
        
        # Calcular Edad
        try:
            # Asume fecha_nacimiento está en formato "DD-MM-AAAA" o similar
            nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            self.edad = datetime.now().year - nacimiento.year
        except ValueError:
            print(" Error: Formato de fecha de nacimiento inválido. Edad asumida como 18.")
            self.edad = 18

        # Calcular Antigüedad
        self.antiguedad = datetime.now().year - self.anio_ingreso
        
        # Atributo que se determina con un método
        self.categoria = self.determinar_categoria() 

   
    def determinar_categoria(self) -> str:
        # Método 1: Determina la categoría del socio basándose en edad y antigüedad.
        # Reglas: 
        #  Cadete: hasta 16 años , Vitalicio: > 35 años ininterrumpidos como socio, Activo: el resto.
        
        if self.edad <= 16:
            return "Cadete"
        
        if self.antiguedad >= 35:
            return "Vitalicio"
            
        return "Activo"

    def calcular_cuota(self) -> float:
        # Método 2: Calcula la cuota mensual aplicando descuentos según la categoría y si es familiar.
        # Descuentos: Cadete: -20%, Activo: Cuota plena, Vitalicio: -100% (Bonificado), Grupo Familiar: -25% adicional
        
        cuota = self.CUOTA_BASE
        descuento_categoria = 0.0

        if self.categoria == "Cadete":
            descuento_categoria = 0.20
        elif self.categoria == "Vitalicio":
            descuento_categoria = 1.00 # 100% de bonificación

        # Aplicar descuento de categoría
        cuota = cuota * (1 - descuento_categoria)
        
        # Aplicar descuento familiar
        if self.es_familiar and cuota > 0:
            cuota = cuota * (1 - 0.25)
            
        return round(cuota, 2)

# Metod str para describir cada socio
    
    def __str__(self):
        
        es_fam = " (Familiar)" if self.es_familiar else ""
        
        precio_cuota = self.calcular_cuota()
        
        return (f"SOCIO | {self.nombre} (ID: {self.socio_id})\n"
                f"   Categoría: {self.categoria}{es_fam}\n"
                f"   Edad: {self.edad} años | Antigüedad: {self.antiguedad} años\n"
                f"   CUOTA MENSUAL: ${precio_cuota:.2f}")

