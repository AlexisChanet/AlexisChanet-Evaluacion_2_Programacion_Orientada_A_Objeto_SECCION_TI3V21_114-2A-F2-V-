class Vehiculo:
    def __init__(self, identificador, marca, modelo, anio, rendimiento_km_litro):
        # Datos básicos del vehículo
        self.identificador = identificador
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.rendimiento_km_litro = rendimiento_km_litro

    def calcular_consumo(self, distancia_km):
        # Cálculo genérico: litros = distancia / rendimiento
        return distancia_km / self.rendimiento_km_litro

    def get_tipo(self):
        # Tipo base (las clases hijas lo cambiarán)
        return "Vehículo"

    def obtener_descripcion(self):
        # Texto legible con la información del vehículo
        return f"{self.identificador} - {self.marca} {self.modelo} ({self.anio}) [{self.get_tipo()}]"

    def __str__(self):
        # Lo que se muestra cuando hacemos print(objeto)
        return self.obtener_descripcion()
