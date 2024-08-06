Users = []


from apprentice import Apprentice
from instructor import Instructor


def Menu():
    option = int(input("""
Hola, bienvenido al sistema de registro:
Selecione una opcion:
1. Registrar un usuario
2. Cambiar estado de un usuario
3. Listar usuarios activos
4. salir
"""))
    return option

def start():
    option = Menu()
    while True:
        if option == 1:
            internal_option = int(input("""
Vas a registrar un usuario, deseas registrar:
1. Aprendiz
2. Instructor
3. Volver al menu 
"""))
            if internal_option == 1:
                name = input("Ingresa el nombre: ")
                email = input("Ingresa el Email: ")
                document = input("Ingresa el documento: ")
                ficha_number = input("Ingresa el numero de ficha: ")
                apprentice = Apprentice(name, email, document, ficha_number)
                Users.append(apprentice)
                print("Aprendiz agregado exitosamente!")
            elif internal_option == 2:
                name = input("Ingresa el nombre: ")
                email = input("Ingresa el Email: ")
                document = input("Ingresa el documento: ")
                specialty = input("Ingrese la especialidad: ")
                instructor = Instructor(name,email,document,specialty)
                Users.append(instructor)
            elif internal_option == 3:
                option = Menu()
        elif option == 2:
            doc = input("Ingrese el documento del usuario: ")
            user_found = False
            for user in Users:
                if user.document == doc:
                    user.change_state()
                    user_found = True
                    print(f"El estado del usuario con documento: {doc}, ha sido cambiado con exito!")
                if not user_found:
                    print("Usuario no encontrado")
        elif option == 3:
            if user.state() == True:
                print(user.show_info())
        elif option == 4:
            print("saliendo del sistema...")
            break
        else:
            print("Opcion no valida, por favor ingrese una correcta.")
start()
        