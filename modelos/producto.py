class Producto:
    """Clase padre que representa un producto del restaurante."""

    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.__precio = precio  # Encapsulación
        self.disponible = disponible

    # Método para obtener el precio
    def obtener_precio(self):
        return self.__precio

    # Método para modificar el precio
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio debe ser mayor que cero.")

    # Método que será sobrescrito por las clases hijas
    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Disponible: {self.disponible}")
