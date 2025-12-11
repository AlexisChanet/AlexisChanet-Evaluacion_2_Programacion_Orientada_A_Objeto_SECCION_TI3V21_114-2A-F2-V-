from clases.vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, identificador, marca, modelo, anio, rendimiento_km_litro, cantidad_puertas):
        # Usamos el constructor de Vehiculo para los datos comunes
        super().__init__(identificador, marca, modelo, anio, rendimiento_km_litro)
        # Dato extra propio del automóvil
        self.cantidad_puertas = cantidad_puertas

    def get_tipo(self):
        # Tipo específico
        return "Automóvil"

    def calcular_consumo(self, distancia_km):
        # Mismo cálculo base por ahora
        return super().calcular_consumo(distancia_km)
