class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        # clave = rut del trabajador, valor = objeto Empleado (o hijo)
        self.trabajadores = {}

    def agregar_trabajador(self, trabajador):
        # Evita ruts repetidos
        if trabajador.rut in self.trabajadores:
            print(f"Ya existe un trabajador con RUT {trabajador.rut}.")
            return
        self.trabajadores[trabajador.rut] = trabajador

    def marcar_inactivo(self, rut):
        # Cambiar estado de un trabajador a inactivo
        trabajador = self.trabajadores.get(rut)
        if trabajador:
            trabajador.activo = False
        else:
            print(f"No se encontró trabajador con RUT {rut}.")

    def buscar_trabajador(self, rut):
        # Devuelve el trabajador o None si no existe
        return self.trabajadores.get(rut)

    def generar_reporte(self):
        # Mostrar resumen de todos los trabajadores
        print(f"=== Reporte de trabajadores de {self.nombre} ===")
        if not self.trabajadores:
            print("No hay trabajadores registrados.")
            return

        for trabajador in self.trabajadores.values():
            print(trabajador)

    def calcular_gasto_total(self):
        # Suma sueldos finales de todos los trabajadores activos
        total = 0
        for trabajador in self.trabajadores.values():
            if trabajador.activo:
                total += trabajador.calcular_sueldo()
        return total
