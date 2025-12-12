from clases.empleado import Empleado

class Practicante(Empleado):
    def __init__(self, rut, nombre_completo, sueldo_base, horas_trabajadas, valor_hora, activo=True):
        # sueldo_base acá puede representar un tope o referencia, pero el sueldo real se calcula por horas
        super().__init__(rut, nombre_completo, sueldo_base, activo)
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def get_tipo(self):
        return "Practicante"

    def calcular_sueldo(self):
        # Sueldo final = horas trabajadas * valor por hora
        return int(self.horas_trabajadas * self.valor_hora)
