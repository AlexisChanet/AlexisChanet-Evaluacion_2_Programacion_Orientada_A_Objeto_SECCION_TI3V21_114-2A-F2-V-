from clases.empleado import Empleado

class Vendedor(Empleado):
    def __init__(self, rut, nombre_completo, sueldo_base, ventas_mes, porcentaje_comision, activo=True):
        # Datos comunes del empleado
        super().__init__(rut, nombre_completo, sueldo_base, activo)
        # Datos propios del vendedor
        self.ventas_mes = ventas_mes              # monto total vendido en el mes
        self.porcentaje_comision = porcentaje_comision  # ej: 0.05 = 5%

    def get_tipo(self):
        return "Vendedor"

    def calcular_sueldo(self):
        # Sueldo final = sueldo base + comisión sobre las ventas
        comision = self.ventas_mes * self.porcentaje_comision
        return int(self.sueldo_base + comision)
