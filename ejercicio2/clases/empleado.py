class Empleado:
    def __init__(self, rut, nombre_completo, sueldo_base, activo=True):
        # Datos básicos del trabajador
        self.rut = rut
        self.nombre_completo = nombre_completo
        self.sueldo_base = sueldo_base
        self.activo = activo

    def get_tipo(self):
        # Las clases hijas devolverán un tipo específico
        return "Empleado"

    def calcular_sueldo(self):
        # Empleado base: solo sueldo base
        return self.sueldo_base

    def obtener_resumen(self):
        # Texto legible con los datos principales
        estado = "Activo" if self.activo else "Inactivo"
        sueldo_final = self.calcular_sueldo()
        return (
            f"{self.rut} - {self.nombre_completo} "
            f"[{self.get_tipo()}] | Base: ${self.sueldo_base} | "
            f"Final: ${sueldo_final} | {estado}"
        )

    def __str__(self):
        return self.obtener_resumen()
