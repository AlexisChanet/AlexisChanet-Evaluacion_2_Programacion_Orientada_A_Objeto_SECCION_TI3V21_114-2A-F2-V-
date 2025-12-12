from .producto import Producto

class ProductoDigital(Producto):
    def __init__(self, codigo, nombre, precio_unitario, stock, tamano_mb, tipo_licencia):
        super().__init__(codigo, nombre, precio_unitario, stock)
        self.tamano_mb = tamano_mb
        self.tipo_licencia = tipo_licencia  # "personal" o "comercial"

    def get_tipo(self):
        return "Digital"

    def calcular_recargo(self, cantidad):
        recargos = {
            "personal": 0,
            "comercial": 5000
        }
        return recargos.get(self.tipo_licencia.lower(), 0)
