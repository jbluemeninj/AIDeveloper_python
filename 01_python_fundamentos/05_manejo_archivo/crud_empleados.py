#Crear un crud de empleado que guarde la informacion en un archivo.
"""
Los modos de apertura más comunes son:
'r': Lectura (por defecto).
'w': Escritura (sobreescribe el archivo si existe).
'a': Añadir (añade al final del archivo).
'r+': Lectura y escritura.

Leer:
 read(): Lee todo el contenido del archivo en una sola cadena.
 readline(): Lee una línea del archivo.
 readlines(): Lee todas las líneas del archivo y las devuelve como una lista.
Escribir:
 write(string): Escribe una cadena en el archivo.
"""

def registrar_empleado():
    with open("empleados.txt", "a") as archivo:
        codigo_empleado = input("Ingresa el codigo del empleado: ")
        nombre = input("Ingresa el nombre del empleado: ")
        cargo = input("Ingresa el cargo del empleado: ")
        salario = input("Ingresa el salario del empleado: ")
        archivo.write(f"{codigo_empleado},{nombre},{cargo},{salario}\n")

def mostrar_empleados():
    with open("empleados.txt", "r") as archivo:
        print(archivo.read())

def eliminar_empleado():
    codigo_empleado = input("Ingresa el codigo del empleado a eliminar: ")
    with open("empleados.txt", "r") as archivo:
        empleados = archivo.readlines()
    with open("empleados.txt", "w") as archivo:
        for empleado in empleados:
            if empleado.split(",")[0] != codigo_empleado:
                archivo.write(empleado)

def actualizar_empleado():
    codigo_empleado = input("Ingresa el codigo del empleado a actualizar: ")
    with open("empleados.txt", "r") as archivo:
        empleados = archivo.readlines()
    with open("empleados.txt", "w") as archivo:
        for empleado in empleados:
            if empleado.split(",")[0] == codigo_empleado:
                nombre = input("Ingresa el nuevo nombre del empleado: ")
                cargo = input("Ingresa el nuevo cargo del empleado: ")
                salario = input("Ingresa el nuevo salario del empleado: ")
                archivo.write(f"{codigo_empleado}, {nombre}, {cargo}, {salario}\n")
            else:
                archivo.write(empleado)

def interface_usuario():
    while True:
        print("1. Registrar empleado")
        print("2. Mostrar empleados")
        print("3. Eliminar empleado")
        print("4. Actualizar empleado")
        print("5. Salir")
        opcion = input("Ingresa una opcion: ")
        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            eliminar_empleado()
        elif opcion == "4":
            actualizar_empleado()
        elif opcion == "5":
            break
        else:
            print("Opcion invalida")

interface_usuario()

