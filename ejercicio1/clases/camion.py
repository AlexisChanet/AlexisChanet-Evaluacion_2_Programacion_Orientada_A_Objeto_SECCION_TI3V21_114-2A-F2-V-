from clases.vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, identificador, marca, modelo, anio, rendimiento_km_litro, capacidad_carga_ton):
        # Datos comunes del vehículo
        super().__init__(identificador, marca, modelo, anio, rendimiento_km_litro)
        # Dato extra propio del camión (en toneladas)
        self.capacidad_carga_ton = capacidad_carga_ton

    def get_tipo(self):
        # Tipo específico
        return "Camión"

    def calcular_consumo(self, distancia_km):
        # Los camiones consumen más según la capacidad de carga
        consumo_base = super().calcular_consumo(distancia_km)
        # Aumentamos el consumo un 5% por cada tonelada de capacidad
        factor = 1 + (self.capacidad_carga_ton * 0.05)
        return consumo_base * factor
