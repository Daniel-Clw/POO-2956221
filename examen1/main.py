
from electronico import Electronico
from ropa import Ropa


ListProductos = []
while True:
    option = int(input("""
Bienvenido al sistema de gestion de productos.
Elija una opcion:
1. Registrar Producto
2. Consultar producto por codigo
3. listar todos los productos
4. Listar productos que tienen cantidad 0
5. Salir
"""))
    if option == 1:
        internal_option = int(input("""
Vas a registrar un producto, seleccione:
1. Electronico
2. Ropa
"""))
        codigo = input("Ingrese el codigo del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("ingrese el precio del producto: "))
        cantidad = int(input("ingrese la cantidad del producto: "))
        if internal_option == 1:
            marca = input("Ingrese la marca del producto: ")
            garantia = int(input("Ingrese la garantia(en MESES) del producto: "))
            electronico = Electronico(codigo, nombre, precio, cantidad, marca, garantia)
            ListProductos.append(electronico)
            print("Produto agregado con exito!")
        elif internal_option == 2:
            talla = input("Ingrese la talla del producto: ")
            material = input("Ingrese el material del producto: ")
            ropa = Ropa(codigo, nombre, precio, cantidad, talla, material)
            ListProductos.append(ropa)
            print("Produto agregado con exito!")
    elif option == 2:
        cod = input("Ingresa el codigo del producto a consultar: ")
        for i in ListProductos:
            if cod == i.codigo:
                print(i.mostrar_info())
    elif option == 3:
        for i in ListProductos:
            print(i.mostrar_info())
    elif option == 4: 
        for i in ListProductos:
            if i.cantidad == 0:
                print(i.mostrar_info())
    elif option == 5:
        print("Saliendo del sistema...")
        break

