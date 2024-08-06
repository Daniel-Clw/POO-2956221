class Productos:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def mostrar_info(self):
        return f"Codigo: {self.codigo}\nNombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}"
    