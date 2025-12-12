class Producto:
    def __init__(self, codigo, nombre, precio_unitario, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def get_tipo(self):
        return "Producto"

    def validar_cantidad(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        if cantidad > self.stock:
            raise ValueError(f"No hay stock suficiente de {self.nombre}. Stock disponible: {self.stock}.")

    def calcular_subtotal(self, cantidad):
        return self.precio_unitario * cantidad

    def calcular_recargo(self, cantidad):
        return 0

    def calcular_total(self, cantidad):
        self.validar_cantidad(cantidad)
        return self.calcular_subtotal(cantidad) + self.calcular_recargo(cantidad)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} [{self.get_tipo()}] | ${self.precio_unitario} | Stock: {self.stock}"
