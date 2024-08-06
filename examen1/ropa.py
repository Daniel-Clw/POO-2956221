from productos import Productos


class Ropa(Productos):
    def __init__(self, codigo, nombre, precio, cantidad, talla, material):
        super().__init__(codigo, nombre, precio, cantidad)
        self.talla = talla
        self.material = material

    def mostrar_info(self):
        return f"Codigo: {self.codigo}\nNombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}\nTalla: {self.talla}\nMaterial: {self.material}"