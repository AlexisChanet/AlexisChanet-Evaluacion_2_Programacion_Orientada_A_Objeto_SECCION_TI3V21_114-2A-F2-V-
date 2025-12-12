from clases.vendedor import Vendedor
from clases.gerente import Gerente
from clases.practicante import Practicante
from clases.empresa import Empresa

def main():
    # Crear la empresa
    empresa = Empresa("Empresa Demo")

    # Crear trabajadores de distintos tipos
    vendedor1 = Vendedor(
        rut="19.553.258-0",
        nombre_completo="Ana Pérez",
        sueldo_base=800000,
        ventas_mes=5000000,
        porcentaje_comision=0.05  # 5% de comisión
    )

    gerente1 = Gerente(
        rut="22.453.575-1",
        nombre_completo="Carlos Gómez",
        sueldo_base=1500000,
        bono_gerencia=300000
    )

    practicante1 = Practicante(
        rut="18.859.325-K",
        nombre_completo="Luis Soto",
        sueldo_base=0,           # aquí no usamos sueldo_base, se calcula por hora
        horas_trabajadas=80,     # horas en el mes
        valor_hora=5000          # paga por hora
    )

    # Registrar trabajadores en la empresa
    empresa.agregar_trabajador(vendedor1)
    empresa.agregar_trabajador(gerente1)
    empresa.agregar_trabajador(practicante1)

    # Ejemplo: marcar inactivo al practicante
    empresa.marcar_inactivo("18.859.325-K")

    # Generar reporte de trabajadores
    empresa.generar_reporte()

    # Calcular y mostrar gasto total mensual (solo activos)
    gasto_total = empresa.calcular_gasto_total()
    print(f"\nGasto total mensual (solo activos): ${gasto_total}")

if __name__ == "__main__":
    main()
