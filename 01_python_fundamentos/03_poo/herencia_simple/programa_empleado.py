
from empleado import Empleado

#Crear una lista de empleados
empleados = [
    Empleado(1,"Ana", "Pérez", 50000),
    Empleado(2,"Juan", "Gómez", 60000),
    Empleado(3,"María", "López", 55000)
]


#Metodo agregar empleado
def agregar_empleado():
    id = len(empleados) + 1
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    nuevo_empleado = Empleado(id,nombre, apellido, salario)
    empleados.append(nuevo_empleado)
    print("Empleado agregado correctamente.")
    mostrar_empleados()

def mostrar_empleados():
    for empleado in empleados:
        print(empleado)


def actualizar_empleado():

    id = int(input("Ingrese el ID del empleado a actualizar: "))
    for empleado in empleados:
        if empleado.get_id() == id:
            nombre = input("Ingrese el nuevo nombre del empleado: ")
            apellido = input("Ingrese el nuevo apellido del empleado: ")
            salario = float(input("Ingrese el nuevo salario del empleado: "))
            empleado.nombre = nombre
            empleado._apellido = apellido
            #empleado.__Empleado__salario = salario
            empleado.set_salario(salario)
            print("Empleado actualizado correctamente.")
            mostrar_empleados()
            return
    print("Empleado no encontrado.")



actualizar_empleado()