class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        # clave = número de cuenta, valor = objeto Cuenta (o hija)
        self.cuentas = {}

    def agregar_cuenta(self, cuenta):
        # Agrega una cuenta solo si el número no existe
        if cuenta.numero_cuenta in self.cuentas:
            print(f"Ya existe una cuenta con número {cuenta.numero_cuenta}.")
            return
        self.cuentas[cuenta.numero_cuenta] = cuenta

    def existe_cuenta(self, numero_cuenta):
        # Verifica si una cuenta existe
        return numero_cuenta in self.cuentas

    def buscar_cuenta(self, numero_cuenta):
        # Devuelve la cuenta o None
        return self.cuentas.get(numero_cuenta)

    def mostrar_cuentas(self):
        # Muestra un resumen de todas las cuentas del banco
        print(f"=== Cuentas del banco {self.nombre} ===")
        if not self.cuentas:
            print("No hay cuentas registradas.")
            return

        for cuenta in self.cuentas.values():
            print(cuenta)

    def obtener_saldo_total(self):
        # Suma el saldo de todas las cuentas
        total = 0
        for cuenta in self.cuentas.values():
            total += cuenta.saldo
        return total
