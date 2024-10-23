class Estudiante:



    def __init__(self, id_estudiante=None, nombre=None, apellido=None, telefono=None, email=None):
        self.id_estudiante= id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Estudiante: ID: {self.id_estudiante}, {self.nombre} {self.apellido}, Telefono: {self.telefono}, Email: {self.email}"
