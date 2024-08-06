class User:
    state = True
    
    def __init__(self, name, email, document):
        self.name= name
        self.email = email
        self.document = document
    
    def change_state(self):
        self.state = False
        return self.state

    def show_info(self):
        return f"Nombre: {self.name}\nCorreo: {self.email}\nDocumento: {self.document}"