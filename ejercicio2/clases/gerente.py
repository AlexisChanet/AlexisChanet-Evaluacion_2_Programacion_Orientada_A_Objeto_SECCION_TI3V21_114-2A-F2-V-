from clases.empleado import Empleado

class Gerente(Empleado):
    def __init__(self, rut, nombre_completo, sueldo_base, bono_gerencia, activo=True):
        super().__init__(rut, nombre_completo, sueldo_base, activo)
        # Monto fijo extra por ser gerente
        self.bono_gerencia = bono_gerencia

    def get_tipo(self):
        return "Gerente"

    def calcular_sueldo(self):
        # Sueldo final = sueldo base + bono de gerencia
        return int(self.sueldo_base + self.bono_gerencia)
