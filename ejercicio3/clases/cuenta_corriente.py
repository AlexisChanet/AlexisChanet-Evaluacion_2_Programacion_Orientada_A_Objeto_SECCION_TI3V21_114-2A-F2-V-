from .cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, titular, saldo_inicial=0, linea_credito=0):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        # Monto máximo que puede quedar en negativo
        self.linea_credito = linea_credito

    def get_tipo(self):
        return "Cuenta Corriente"

    def puede_retirar(self, monto):
        # Permite sobregiro hasta la línea de crédito
        saldo_final = self.saldo - monto
        return saldo_final >= -self.linea_credito
