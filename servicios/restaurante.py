class Restaurante:
    """Clase que administra los productos."""

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("\n=========== PRODUCTOS DEL RESTAURANTE ===========")

        if not self.productos:
            print("No existen productos registrados.")
            return

        for producto in self.productos:
            producto.mostrar_informacion()
