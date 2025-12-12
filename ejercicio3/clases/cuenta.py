class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        # Datos básicos de la cuenta
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial
        # Historial de movimientos (lista de textos)
        self.movimientos = []

    def get_tipo(self):
        # Las clases hijas cambiarán este texto
        return "Cuenta"

    def registrar_movimiento(self, descripcion):
        # Guarda un texto legible en el historial
        self.movimientos.append(descripcion)

    def depositar(self, monto):
        # Depósito simple
        if monto <= 0:
            print("El monto a depositar debe ser positivo.")
            return
        self.saldo += monto
        self.registrar_movimiento(f"DEPÓSITO: +${monto} | Saldo: ${self.saldo}")

    def puede_retirar(self, monto):
        # Regla genérica: no permitir saldo negativo
        return self.saldo - monto >= 0

    def retirar(self, monto):
        # Retiro con validación según el tipo de cuenta
        if monto <= 0:
            print("El monto a retirar debe ser positivo.")
            return

        if self.puede_retirar(monto):
            self.saldo -= monto
            self.registrar_movimiento(f"RETIRO: -${monto} | Saldo: ${self.saldo}")
        else:
            print(f"No es posible retirar ${monto} desde la {self.get_tipo()} {self.numero_cuenta}.")

    def obtener_resumen(self):
        # Información resumida de la cuenta
        return f"{self.numero_cuenta} - {self.titular} [{self.get_tipo()}] | Saldo: ${self.saldo}"

    def mostrar_historial(self):
        # Muestra todos los movimientos en orden
        print(f"Historial de movimientos de la cuenta {self.numero_cuenta}:")
        if not self.movimientos:
            print("  Sin movimientos registrados.")
            return

        for mov in self.movimientos:
            print("  " + mov)

    def __str__(self):
        return self.obtener_resumen()
