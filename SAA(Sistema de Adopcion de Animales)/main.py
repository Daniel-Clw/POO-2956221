from SAA import Animal

animals_list = []

while True:
        print("""
1. Agregar animal
2. Mostrar información de un animal
3. Actualizar nombre de un animal
4. Mostrar todos los animales registrados
5. Mostrar animales en riesgo
6. Adoptar un animal
7. Eliminar un animal
8. Salir""")
        option = input("Ingrese su opción: ")
        
        if option == "1":
            code, name, age, species, breed = "", "", "", "", ""
            while not code:
                code = input("Ingrese el código del animal: ")
            while not name:
                name = input("Ingrese el nombre del animal: ")
            while not age:
                try:
                    age = int(input("Ingrese la edad del animal: "))
                except ValueError:
                    print("Entrada no válida. La edad debe ser un número.")
                    age = ""
            while not species:
                species = input("Ingrese la especie del animal (perro/gato): ")
                if species not in ["dog", "cat"]:
                    print("Especie no válida. Debe ser 'perro' o 'gato'.")
                    species = ""
            while not breed:
                breed = input("Ingrese la raza del animal: ")
            animal = Animal.create_animal(code, name, age, species, breed)
            animals_list.append(animal)
            print("Animal agregado exitosamente.")
        
        elif option == "2":
            code = input("Ingrese el código del animal: ")
            animal = Animal.search_by_code(code, animals_list)
            if animal:
                animal.info()
            else:
                print("Animal no encontrado.")
        
        elif option == "3":
            code = input("Ingrese el código del animal: ")
            animal = Animal.search_by_code(code, animals_list)
            if animal:
                new_name = input("Ingrese el nuevo nombre: ")
                animal.update_name(new_name)
                print("Nombre actualizado exitosamente.")
            else:
                print("Animal no encontrado.")
        
        elif option == "4":
            Animal.show_all(animals_list)
        
        elif option == "5":
            Animal.animals_risk(animals_list)
        
        elif option == "6":
            code = input("Ingrese el código del animal: ")
            animal = Animal.search_by_code(code, animals_list)
            if animal:
                animal.adopt()
                print("Animal adoptado exitosamente.")
            else:
                print("Animal no encontrado.")
        
        elif option == "7":
            code = input("Ingrese el código del animal: ")
            animal = Animal.search_by_code(code, animals_list)
            if animal:
                animal.delete(animals_list)
                print("Animal eliminado exitosamente.")
            else:
                print("Animal no encontrado.")
        
        elif option == "8":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor intente de nuevo.")
