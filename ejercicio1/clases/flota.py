class Flota:
    def __init__(self):
        # Usamos un diccionario: clave = identificador, valor = objeto vehículo
        self.vehiculos = {}

    def agregar_vehiculo(self, vehiculo):
        # Agrega un vehículo si el identificador no existe
        if vehiculo.identificador in self.vehiculos:
            print(f"Ya existe un vehículo con identificador {vehiculo.identificador}.")
            return
        self.vehiculos[vehiculo.identificador] = vehiculo

    def eliminar_vehiculo(self, identificador):
        # Elimina un vehículo por identificador, si existe
        if identificador in self.vehiculos:
            del self.vehiculos[identificador]
        else:
            print(f"No se encontró vehículo con identificador {identificador}.")

    def buscar_vehiculo(self, identificador):
        # Devuelve el vehículo si existe, si no devuelve None
        return self.vehiculos.get(identificador)

    def calcular_consumo_total(self, distancia_km):
        # Suma el consumo de todos los vehículos para la distancia indicada
        consumo_total = 0
        for vehiculo in self.vehiculos.values():
            consumo_total += vehiculo.calcular_consumo(distancia_km)
        return consumo_total

    def listar_consumos(self, distancia_km):
        # Devuelve una lista con el consumo individual de cada vehículo
        resultados = []
        for vehiculo in self.vehiculos.values():
            consumo = vehiculo.calcular_consumo(distancia_km)
            resultados.append((vehiculo.identificador, vehiculo.get_tipo(), consumo))
        return resultados

    def mostrar_flota(self):
        # Muestra la descripción de todos los vehículos
        for vehiculo in self.vehiculos.values():
            print(vehiculo)
