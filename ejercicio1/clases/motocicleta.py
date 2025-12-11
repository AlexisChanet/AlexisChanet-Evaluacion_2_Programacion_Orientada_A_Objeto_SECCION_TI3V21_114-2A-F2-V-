from clases.vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, identificador, marca, modelo, anio, rendimiento_km_litro, cilindrada_cc):
        # Datos comunes del vehículo
        super().__init__(identificador, marca, modelo, anio, rendimiento_km_litro)
        # Dato extra propio de la moto
        self.cilindrada_cc = cilindrada_cc

    def get_tipo(self):
        # Tipo específico
        return "Motocicleta"

    def calcular_consumo(self, distancia_km):
        # Supongamos que las motos son un poco más eficientes (ajustamos un poco el consumo)
        consumo_base = super().calcular_consumo(distancia_km)
        return consumo_base * 0.9  # consume un 10% menos que el cálculo genérico
