from clases.cuenta_corriente import CuentaCorriente
from clases.cuenta_ahorro import CuentaAhorro
from clases.banco import Banco

def main():
    banco = Banco("Banco Demo")

    # Crear cuentas (2 corrientes y 2 de ahorro)
    cuenta_corriente_1 = CuentaCorriente("1001", "Akira Kurosawa", 500000, 200000)
    cuenta_corriente_2 = CuentaCorriente("1002", "Shigeru Miyamoto", 200000, 100000)

    cuenta_ahorro_1 = CuentaAhorro("2001", "Pharrell Williams", 1000000, 0.01)
    cuenta_ahorro_2 = CuentaAhorro("2002", "Ada Lovelace", 300000, 0.02)

    # Agregar cuentas al banco
    banco.agregar_cuenta(cuenta_corriente_1)
    banco.agregar_cuenta(cuenta_corriente_2)
    banco.agregar_cuenta(cuenta_ahorro_1)
    banco.agregar_cuenta(cuenta_ahorro_2)

    print("Cuentas registradas en el banco:")
    banco.mostrar_cuentas()

    # Movimientos cuenta corriente 1
    print("\nMovimientos cuenta corriente 1001")
    cuenta_corriente_1.depositar(100000)
    cuenta_corriente_1.retirar(650000)    # puede usar línea de crédito
    cuenta_corriente_1.retirar(2000000)   # debería rechazarse
    cuenta_corriente_1.mostrar_historial()

    # Movimientos cuenta corriente 2
    print("\nMovimientos cuenta corriente 1002")
    cuenta_corriente_2.retirar(250000)    # usa parte de la línea de crédito
    cuenta_corriente_2.depositar(50000)
    cuenta_corriente_2.mostrar_historial()

    # Movimientos cuenta ahorro 1
    print("\nMovimientos cuenta ahorro 2001")
    cuenta_ahorro_1.depositar(200000)
    cuenta_ahorro_1.retirar(500000)
    cuenta_ahorro_1.aplicar_interes_mensual()
    cuenta_ahorro_1.mostrar_historial()

    # Movimientos cuenta ahorro 2
    print("\nMovimientos cuenta ahorro 2002")
    cuenta_ahorro_2.depositar(50000)
    cuenta_ahorro_2.aplicar_interes_mensual()
    cuenta_ahorro_2.mostrar_historial()

    # Buscar una cuenta y mostrar su información (ejemplo: 2001)
    print("\nConsulta de la cuenta 2001")
    cuenta_buscada = banco.buscar_cuenta("2001")
    if cuenta_buscada is not None:
        print(cuenta_buscada.obtener_resumen())
        cuenta_buscada.mostrar_historial()
    else:
        print("No se encontró la cuenta 2001")

    # Mostrar el saldo total del banco
    saldo_total = banco.obtener_saldo_total()
    print(f"\nSaldo total administrado por el banco: ${saldo_total}")

if __name__ == "__main__":
    main()
