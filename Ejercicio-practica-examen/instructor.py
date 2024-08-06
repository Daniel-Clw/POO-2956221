from user import User


class Instructor(User):
    def __init__(self, name, email, document, specialty):
        super().__init__(name, email, document)
        self.specialty = specialty

    def show_info(self):
        return f"Nombre: {self.name}\nCorreo: {self.email}\nDocumento: {self.document}\nEspecialidad: {self.specialty} "