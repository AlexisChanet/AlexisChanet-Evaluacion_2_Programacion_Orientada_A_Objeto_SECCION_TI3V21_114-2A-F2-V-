class Carrito:
    def __init__(self):
        # codigo -> {"producto": obj, "cantidad": int}
        self.items = {}

    def agregar_producto(self, producto, cantidad):
        producto.validar_cantidad(cantidad)

        cantidad_actual = self.items.get(producto.codigo, {"cantidad": 0})["cantidad"]
        nueva_cantidad = cantidad_actual + cantidad

        if nueva_cantidad > producto.stock:
            raise ValueError(
                f"No hay stock suficiente de {producto.nombre}. Stock: {producto.stock}, en carrito: {cantidad_actual}."
            )

        if producto.codigo in self.items:
            self.items[producto.codigo]["cantidad"] = nueva_cantidad
        else:
            self.items[producto.codigo] = {"producto": producto, "cantidad": cantidad}

    def eliminar_producto(self, codigo):
        if codigo not in self.items:
            raise ValueError("El producto no está en el carrito.")
        del self.items[codigo]

    def obtener_detalle(self):
        detalle = []
        for item in self.items.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            total_producto = producto.calcular_total(cantidad)

            detalle.append({
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "tipo": producto.get_tipo(),
                "cantidad": cantidad,
                "total": total_producto
            })
        return detalle

    def calcular_totales(self):
        subtotal = 0
        recargos = 0

        for item in self.items.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            subtotal += producto.calcular_subtotal(cantidad)
            recargos += producto.calcular_recargo(cantidad)

        return subtotal, recargos, subtotal + recargos

    def confirmar_compra(self):
        for item in self.items.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            if cantidad > producto.stock:
                raise ValueError(f"Compra rechazada: sin stock suficiente de {producto.nombre}.")

        for item in self.items.values():
            producto = item["producto"]
            cantidad = item["cantidad"]
            producto.stock -= cantidad

        self.items.clear()
