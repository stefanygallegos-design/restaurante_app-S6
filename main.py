from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():

    restaurante = Restaurante()

    # Platillos
    platillo1 = Platillo("Pizza Hawaiana", 9.50, True, 850)
    platillo2 = Platillo("Hamburguesa Especial", 7.25, True, 720)

    # Bebidas
    bebida1 = Bebida("Jugo de Naranja", 2.50, True, 500)
    bebida2 = Bebida("Limonada", 2.00, False, 450)

    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    restaurante.mostrar_productos()


if __name__ == "__main__":
    main()
