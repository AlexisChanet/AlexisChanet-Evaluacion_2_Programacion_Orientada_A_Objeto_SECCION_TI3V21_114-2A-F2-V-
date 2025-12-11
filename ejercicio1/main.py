from clases.automovil import Automovil
from clases.motocicleta import Motocicleta
from clases.camion import Camion
from clases.flota import Flota

def main():
    # Crear algunos vehículos de ejemplo
    auto1 = Automovil(
        identificador="A001",
        marca="Honda",
        modelo="Civic",
        anio=2020,
        rendimiento_km_litro=15,
        cantidad_puertas=4
    )

    moto1 = Motocicleta(
        identificador="M001",
        marca="Yamaha",
        modelo="MT-03",
        anio=2022,
        rendimiento_km_litro=25,
        cilindrada_cc=321
    )

    camion1 = Camion(
        identificador="C001",
        marca="Volvo",
        modelo="FH",
        anio=2019,
        rendimiento_km_litro=5,
        capacidad_carga_ton=10
    )

    # Crear la flota y agregar los vehículos
    flota = Flota()
    flota.agregar_vehiculo(auto1)
    flota.agregar_vehiculo(moto1)
    flota.agregar_vehiculo(camion1)

    # Mostrar información de todos los vehículos
    print("=== Flota de vehículos ===")
    flota.mostrar_flota()

    # Definir un trayecto común
    distancia = 150  # km
    print(f"\n=== Consumos para un trayecto de {distancia} km ===")

    # Listar consumos individuales
    consumos = flota.listar_consumos(distancia)
    for identificador, tipo, consumo in consumos:
        print(f"{identificador} ({tipo}) -> {consumo:.2f} litros")

    # Calcular consumo total de la flota
    consumo_total = flota.calcular_consumo_total(distancia)
    print(f"\nConsumo total de la flota para {distancia} km: {consumo_total:.2f} litros")

if __name__ == "__main__":
    main()
