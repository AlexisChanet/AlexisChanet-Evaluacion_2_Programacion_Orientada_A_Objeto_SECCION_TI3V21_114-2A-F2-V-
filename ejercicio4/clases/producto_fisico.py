from .producto import Producto

class ProductoFisico(Producto):
    def __init__(self, codigo, nombre, precio_unitario, stock, peso_kg, categoria_envio):
        super().__init__(codigo, nombre, precio_unitario, stock)
        self.peso_kg = peso_kg
        self.categoria_envio = categoria_envio  # "liviano", "estandar", "pesado"

    def get_tipo(self):
        return "Físico"

    def calcular_recargo(self, cantidad):
        tarifas = {
            "liviano": 1000,
            "estandar": 2500,
            "pesado": 5000
        }
        envio_unitario = tarifas.get(self.categoria_envio, 2500)
        return envio_unitario * cantidad
