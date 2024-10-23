#Crear una clase administrador que herede de empleado

from empleado import Empleado

class Administrador(Empleado):

    #Metodo constructor
    def __init__(self, codigo,nombre, apellido, salario, oficina):
        super().__init__(codigo,nombre, apellido, salario)
        self.oficina = oficina



    #Metodo str
    def __str__(self):
        return f"Administrador: {self.nombre} {self._apellido}, Salario: {self.get_salario()}"