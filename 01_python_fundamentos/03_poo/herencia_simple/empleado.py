#Crear una clase Empleado
#Crear sus atributos : nombre, apellido, salario (publicos, protegido, privado)
#Crear metodo constructor
#Crear str
#Crear metodo setter y getter para salario y apellido

class Empleado:

   #Metodo constructor
    def __init__(self, id,nombre, apellido, salario):
        self.__id = id
        self.nombre = nombre #publico
        self._apellido = apellido #protegido
        self.__salario = salario #privado

   #Metodos Getter y setter
    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_id(self):
        return self.__id

    #Metodo saludar
    def hablar(self):
        print("Hola soy un empleado")


    #Metodo imprimir
    def __str__(self):
        return f"Empleado: Codigo: {self.__id} , {self.nombre} {self._apellido}, Salario: {self.__salario}"