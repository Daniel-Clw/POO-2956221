#El ejercicio consta de un sistema de adopcion para animales (perros y gatos)cada animal debe tener un code, name, species,breed y adopted que estara por default en false este debe cambiar a verdadero luego de que un animal sea adoptado


#Primero creare la clase animal y sus atributos 

class Animal:
    def __init__(self, code, name, age, species, breed):
        self.code = code
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.adopted = False  # El atributo por defecto es False porque no ha sido adoptado.

    def info(self):
        print(f"Animal No°: {self.code}\nNombre: {self.name}\nEdad: {self.age}\nEspecie: {self.species}\nRaza: {self.breed}\nAdoptado: {'Sí' if self.adopted else 'No'}")
    
    def adopt(self):
        self.adopted = True
    
    def update_name(self, name):
        self.name = name

    @classmethod
    def create_animal(cls, code, name, age, species, breed):
        return cls(code, name, age, species, breed)
    
    def delete(self, animals_list):
        animals_list.remove(self)
    
    @staticmethod
    def search_by_code(code, animals_list):
        for animal in animals_list:
            if animal.code == code:
                return animal
        return None
    
    @staticmethod
    def show_all(animals_list):
        for animal in animals_list:
            animal.info()
    
    @staticmethod
    def animals_risk(animals_list):
        for animal in animals_list:
            if animal.age > 10:
                print(f"Código: {animal.code}, Nombre: {animal.name}")

