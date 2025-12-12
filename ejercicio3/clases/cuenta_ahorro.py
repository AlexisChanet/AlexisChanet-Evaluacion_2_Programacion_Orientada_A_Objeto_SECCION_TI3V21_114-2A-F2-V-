from .cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, titular, saldo_inicial=0, tasa_interes=0.0):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        # Tasa de interés mensual, por ejemplo 0.01 = 1% mensual
        self.tasa_interes = tasa_interes

    def get_tipo(self):
        return "Cuenta de Ahorro"

    def puede_retirar(self, monto):
        # En cuentas de ahorro NO se permite sobregiro
        saldo_final = self.saldo - monto
        return saldo_final >= 0

    def aplicar_interes_mensual(self):
        # Calcula y aplica el interés del mes
        if self.saldo <= 0:
            # No aplica interés si no hay saldo
            return

        interes = int(self.saldo * self.tasa_interes)
        self.saldo += interes
        # Registrar el interés como movimiento
        self.registrar_movimiento(f"INTERÉS: +${interes} | Saldo: ${self.saldo}")
