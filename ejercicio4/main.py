from clases.producto_fisico import ProductoFisico
from clases.producto_digital import ProductoDigital
from clases.carrito import Carrito

def main():
    # Productos físicos
    consola_ps5 = ProductoFisico(
        "CONSOLE001",
        "Consola PlayStation 5",
        499990,
        10,
        peso_kg=4.5,
        categoria_envio="pesado"
    )

    audifonos_hyperx = ProductoFisico(
        "ACCES001",
        "Audífonos HyperX Cloud II",
        79990,
        15,
        peso_kg=0.4,
        categoria_envio="liviano"
    )

    # Productos digitales
    juego_clair_obscur = ProductoDigital(
        "GAME001",
        "Clair Obscur: Expedition 33",
        39990,
        50,
        tamano_mb=60000,
        tipo_licencia="personal"
    )

    xbox_live_gold = ProductoDigital(
        "SUBS001",
        "Xbox Live Gold 12 meses",
        119990,
        30,
        tamano_mb=10,
        tipo_licencia="comercial"
    )

    print("Productos disponibles:")
    print(consola_ps5)
    print(audifonos_hyperx)
    print(juego_clair_obscur)
    print(xbox_live_gold)

    carrito = Carrito()

    print("\nAgregando productos al carrito...")
    try:
        carrito.agregar_producto(consola_ps5, 1)
        carrito.agregar_producto(audifonos_hyperx, 2)
        carrito.agregar_producto(juego_clair_obscur, 1)
        carrito.agregar_producto(xbox_live_gold, 1)

        # Prueba de validación: exceder stock
        carrito.agregar_producto(audifonos_hyperx, 50)

    except ValueError as e:
        print(f"Error: {e}")

    print("\nDetalle del carrito:")
    for item in carrito.obtener_detalle():
        print(f"- {item['nombre']} [{item['tipo']}] x{item['cantidad']} -> ${item['total']}")

    subtotal, recargos, total = carrito.calcular_totales()
    print(f"\nSubtotal (sin recargos): ${subtotal}")
    print(f"Recargos (envío/licencias): ${recargos}")
    print(f"Total final a pagar: ${total}")

    print("\nConfirmando compra...")
    try:
        carrito.confirmar_compra()
        print("Compra realizada. Stock actualizado.")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nStock después de la compra:")
    print(consola_ps5)
    print(audifonos_hyperx)
    print(juego_clair_obscur)
    print(xbox_live_gold)

if __name__ == "__main__":
    main()
