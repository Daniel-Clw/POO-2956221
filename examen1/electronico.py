from productos import Productos


class Electronico(Productos):
    def __init__(self, codigo, nombre, precio, cantidad, marca, garantia):
        super().__init__(codigo, nombre, precio, cantidad)
        self.marca = marca
        self.garantia = garantia 

    def mostrar_info(self):
        return f"Codigo: {self.codigo}\nNombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}\nMarca: {self.marca}\nGarantia(en meses): {self.garantia}"
    