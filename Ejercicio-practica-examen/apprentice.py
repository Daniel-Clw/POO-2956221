from user import User


class Apprentice(User):
    def __init__(self, name, email, document,ficha_number):
        super().__init__(name, email, document)
        self.ficha_number = ficha_number

    def show_info(self):
        return f"Nombre: {self.name}\nCorreo: {self.email}\nDocumento: {self.document}\nNumero de ficha: {self.ficha_number}"